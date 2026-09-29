import os
from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv
import pymysql


connection = pymysql.connect(host='localhost',user='root',password='Test@123',port=3306,database='genai_db')

#insert_query = "insert into users(name,email,interested_course,current_status,course_type) values(%s,%s,%s,%s,%s);"

get_query = 'select * from users'

cursor = connection.cursor()

#cursor.execute(insert_query,('super admin','superadmin@gmail.com','ReactJS','Active','Offline'))

cursor.execute(get_query)

data = cursor.fetchall()
print(data)
#connection.commit()

connection.close()

load_dotenv()

app = FastAPI()

@app.post('/api/chat')

def sendQuery():
    return {'message':'Successfully posted the data'}