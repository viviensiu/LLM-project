import os
import time
from embed import Embed
from openai import OpenAI
from elasticsearch import Elasticsearch

class RAG():
    def __init__(self, modelname, apikey=None) -> None:
        self.es_client = Elasticsearch(os.getenv("ELASTICSEARCH_URL"))
        self.index_name = os.getenv("INDEX_NAME")
        # ------- Uncomment for test_rag.py --------------------
        # self.es_client = Elasticsearch("http://localhost:9200")
        # self.index_name = "az900_course_notes"

        self.apikey = apikey
        # apikey = os.getenv("OPENAI_API_KEY")

        if modelname == "1":
            # GPT-4o mini
            self.client = OpenAI(api_key=apikey)
            self.model = "gpt-4o-mini"
        elif modelname == "2":
            self.client = OpenAI(base_url='http://localhost:11434/v1/', api_key='ollama')
            self.model = "phi3"

    def retrieve(self, question, question_vec):
        '''
        Accepts user question and an embedding vector of the same question
        Retrieves relevant context from Elasticsearch index using hybrid search
        '''
        keyword_query = {"query": question,
                        "fields": ["header", "subheader", "doc_text"],
                        "type": "best_fields",
                        "boost": 0.05,
                        }

        vector_query = {"query": {"match_all": {}},
                        "script": {
                                    "source": """
                                        0.2 * cosineSimilarity(params.query_vector, 'header_vec') + 
                                        0.2 * cosineSimilarity(params.query_vector, 'subheader_vec') + 
                                        0.6 * cosineSimilarity(params.query_vector, 'doc_text_vec') + 1
                                    """,
                                    "params": {"query_vector": question_vec}
                                }
                    }
        
        hybrid_query = {
            "bool": {
                "must": [{"multi_match": keyword_query},
                        {"script_score": vector_query}
                        ]
                },
            }

        search_query = {
            "query": hybrid_query,
            "size": 5,
            "_source": ['doc_id', 'header', 'subheader', 'document', 'doc_text']
        }

        es_results = self.es_client.search(
            index=self.index_name,
            body=search_query
        )
        
        result_docs = []
        
        for hit in es_results['hits']['hits']:
            result_docs.append(hit['_source'])

        return result_docs
    
    def augment(self, question, search_results):
        '''
        Accepts a question and search results
        Returns a prompt augmented with question and context generated from search results
        '''
        prompt_template = """
    You're a friendly course instructor helping students to understand topics in the Azure Fundamentals AZ-900 course. Answer the QUESTION based on the CONTEXT in a user-friendly way.
    Use only the information from the CONTEXT to answer the QUESTION. 

    QUESTION: {question}

    CONTEXT: 
    {context}
    """.strip()

        context = ""
        
        for doc in search_results:
            context = context + f"Topic: {doc['header']}\nSub-topic: {doc['subheader']}\nNotes: {doc['doc_text']}\n\n"
        
        prompt = prompt_template.format(question=question, context=context).strip()
        return prompt
    
    def generate(self, prompt):
        '''
        Accepts a prompt and (optional) an OpenAI chat API model of choice
        Returns an LLM response, tokens usage info, and total time for generating response.
        '''
        start_time = time.time()
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        latency = time.time() - start_time
        return response.choices[0].message.content, response.usage, latency
    
    def rag(self, query):
        embedder = Embed()
        question_vec = embedder.embed_text(query)
        print(len(question_vec))
        search_results = self.retrieve(query, question_vec)
        prompt = self.augment(query, search_results)
        response, usage, latency = self.generate(prompt)
        return response, usage, latency