from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

handler = Mangum(app)