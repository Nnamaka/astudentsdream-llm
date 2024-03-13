import os
import boto3
from dotenv import load_dotenv
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM

load_dotenv()
app = FastAPI()

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
access_token = os.environ.get('HUG_ACCES_TOKEN')

try:
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    print("Loaded Amazon client ✅")
except:
    print("Error occured while loading boto3")

s3_bucket_name = "astudentsdreamllm"

model_name = "google/gemma-2b"

# Download the model and tokenizer (if necessary) to your local machine
print("downloading model...😎")
model = AutoModelForCausalLM.from_pretrained(model_name,use_auth_token=access_token)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)

#print("saving the model locally")

#save_path = os.path.join(os.getcwd(), "gamma_model")
#model.save_pretrained(save_path)
#tokenizer.save_pretrained(save_path)

#for root, _, files in os.walk(save_path):
#    for filename in files:
#      local_path = os.path.join(root, filename)
#      s3_path = os.path.relpath(local_path, save_path)
#      s3.upload_file(local_path, s3_bucket_name, s3_path)

#s3.upload_file(filename, s3_bucket_name, filename)


@app.get("/")
def root():
    return {"astudentsdream llm": "underconstruction 🚧"}

