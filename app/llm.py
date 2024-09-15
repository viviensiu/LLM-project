from openai import OpenAI
import os

class LLM:
    def __init__(self, modelname, apikey=None) -> None:
        '''
            Initialise an LLM object for the selected model (GPT or Open Source models)
            Limit to HuggingFace or Ollama for Open Source for now
        '''
        # self.modelname = modelname
        self.apikey = apikey
        apikey = os.getenv("OPENAI_API_KEY")

        if modelname == "1":
            # GPT-4o mini
            self.client = OpenAI(api_key=apikey)
            self.model = "gpt-4o-mini"
        elif modelname == "2":
            self.client = OpenAI(base_url='http://localhost:11434/v1/', api_key='ollama')
            self.model = "phi3"
    
    def respond(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def augment(question, search_results):
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


