import os
import boto3
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

try:
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    print("Loaded Amazon client ✅")
except:
    print("Error occured while loading boto3")

s3_bucket_name = "astudentsdreamllm"



@app.get("/")
def root():
    return {"astudentsdream llm": "underconstruction 🚧"}

