import os
from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)

@app.get('/')
def index():
    return {'message': 'Server is up and running'}

@app.post('/api/login')
def login():
    return {'message': 'Login was successful'}

@app.post('/api/signup')
def signUp():
    return {'message': 'Sign up was successful'}

class RequestData(BaseModel):
    message:str

@app.post('/api/chat')
def chat(request: RequestData):
    prompt = f"""

     You are an AI assistant for softwareschool, we are providing online coding classes in telugu.
     Understand user background, goal and suggest the best courses

    Course 1 : Course Name: ReactJS, Language: Telugu, Mode=Recorded, Validity=lifelong, Scripting Language: Javascript
    Course 2:  Course Name: AI, Language: Telugu, Mode=Live, Validity=lifelong, Scripting Language: Python

    RULES:
    1. Ask any questions one after the other
    2. Keep the answers crisp and short
    3. Be polit and friendly
    4. Use Smilies or Emojis

    user message:
    {request.message}
     """
    ai_response = openai_client.responses.create(input=prompt, model='gpt-4o')
    return {"message": ai_response.output_text}
