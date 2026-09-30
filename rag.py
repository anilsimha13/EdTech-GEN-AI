from fastapi import FastAPI, UploadFile, File
import chromadb
from openai import OpenAI
import os
from dotenv import load_dotenv
import uuid
from pypdf import PdfReader
from docx import Document
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


def process_pdf(file):
    print('Processing PDF')
    pdf_reader = PdfReader(file.file)
    data = ""
    for page in pdf_reader.pages:
        data = data + (page.extract_text() or "")
    return data

def process_doc(file):
    print('Processing Document')
def process_txt(file):
    print('Processing Text file')

@app.post('/api/upload-file')
def upload_file(file:UploadFile=File(...)):

    file_name = file.filename
    process_msg = ""
    if file_name.endswith('.pdf'):
        process_msg = 'Processing PDF'
        data =  process_pdf(file)
    if file_name.endswith('docx') or file_name.endswith('doc'):
        process_msg = 'processing Document'
        process_doc(file)
    if file_name.endswith('.txt'):
        process_msg = 'Processing text file'
        process_txt(file)
    return {'message':'Upload file successful',"file_data":file,"processing_msg":process_msg,'data':data}