from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get('/')
def home():
    return {"Message":"On your Home Page"}

@app.get('/service')
def call_service():

    # reqUrl = os.environ.get('SERVICE_URL')

    # trying using links
    reqUrl = 'http://service:8000/'

    headersList = {"Accept": "*/*"}

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    print(response.text)

    return {'response':f'{response.text}'}



# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000