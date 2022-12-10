from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def service():
    return {"Message":"Response from the service"}

# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000