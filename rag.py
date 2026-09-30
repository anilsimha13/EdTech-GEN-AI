from fastapi import FastAPI
import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv
import uuid

load_dotenv()

app = FastAPI()

chromadb_client = chromadb.PersistentClient('./chroma_db')
courses_collections = chromadb_client.get_or_create_collection(name='courses')

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)

@app.get('/')
def index():
    return {'message':'App is up and running'}


@app.post('/api/add-data')

def add_data():

    data = ['AI','Price:8000','Teaching Mode:Telugu','Recording availibility:True','Programming Language: Python']
    response = []
    for chunks in data:
        print(chunks)
        vectors = openai_client.embeddings.create(input=chunks,model="text-embedding-3-small")
        print(vectors)
        id = uuid.uuid4()
        courses_collections.add(ids=[str(id)],documents=[chunks],embeddings=[vectors.data[0].embedding])
        response.append({"id":str(id),'data':chunks,'vectors':vectors.data[0].embedding})
    return {'message':'Data added successfully','response':response}