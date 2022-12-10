from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {"Message":"On your Home Page"}

# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000