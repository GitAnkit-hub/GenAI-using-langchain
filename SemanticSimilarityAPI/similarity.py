import pandas as pd
import numpy as np
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv


load_dotenv()
embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=300)
def SimiarityCheckAPI(input1, input2):
    

    # q1_embedding = embedding.embed_query(input1)

    # q2_embedding = embedding.embed_query(input2)
    q1_embedding, q2_embedding = embedding.embed_documents([input1, input2])
    scores = cosine_similarity([q1_embedding], [q2_embedding])
    response_dict = {
        'similarity_score': float(scores[0][0]),
        'model': 'text-embedding-3-small',
        'dimensions': 300
    }
    return response_dict