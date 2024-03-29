import os
import boto3
from dotenv import load_dotenv
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM

load_dotenv()
app = FastAPI()

model_name = "google/gemma-2b"
s3_bucket_name = "astudentsdreamllm"
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
access_token = os.environ.get('HUG_ACCES_TOKEN')

try:
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    print("Loaded Amazon client ✅")
except:
    print("Error occured while loading boto3")

model_files = ['config.json', 'generation_config.json', 'model-00001-of-00003.safetensors', 'model-00002-of-00003.safetensors',
              'model-00003-of-00003.safetensors', 'model.safetensors.index.json', 'special_tokens_map.json', 'tokenizer_config.json',
              'tokenizer.json']

# Download the model and tokenizer (if necessary) to your local machine
#print("downloading model...😎")
#model = AutoModelForCausalLM.from_pretrained(model_name,use_auth_token=access_token)
#tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)

model_folder_name = "gamma_model"
current_dir = os.getcwd()
save_path = os.path.join(current_dir, model_folder_name)

if os.path.exists(save_path) and os.listdir(save_path) :
    pass
else :
    os.makedirs(save_path)
    for file in model_files:
        save_here = os.path.join(save_path, file)
        s3.download_file(s3_bucket_name, file, save_here)

model = AutoModelForCausalLM.from_pretrained(save_path )
tokenizer = AutoTokenizer.from_pretrained(save_path)


# saving the model
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

def generate_answer(question):
  inputs = tokenizer(question, return_tensors="pt")  # Tokenize the question
  output = model.generate(**inputs)  # Generate response using the model
  decoded_response = tokenizer.decode(output[0])  # Decode the generated tokens
  return decoded_response

@app.get("/")
def root(question: str):
    try:
        print(question)
        answer = generate_answer(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        return {"error": str(e)} 




