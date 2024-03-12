import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

@app.get("/")
def root():
    return {"astudentsdream llm": "underconstruction 🚧"}

