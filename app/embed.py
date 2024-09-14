from sentence_transformers import SentenceTransformer

class Embed():
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L12-v2') -> None:
        '''
        Initialise an embedding model available from Sentence Transformers package
        '''
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)
    
    def get_embed_model(self):
        '''
        Returns the embedding model
        '''
        return self.model
    
    def get_vec_dim(self):
        '''
        Returns dimensions of the embedding vector
        '''
        return self.model.get_sentence_embedding_dimension()
    
    def embed_text(self, text):
        '''
        Accepts text
        Returns an embedded vector of text
        '''
        return self.model.encode(text)