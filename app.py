from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Server is up and running'}

@app.post('/api/login')
def login():
    return {'message': 'Login was successful'}

@app.post('/api/signup')
def signUp():
    return {'message': 'Sign up was successful'}
