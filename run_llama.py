from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b")
input = "write 450 words on the history of america"

print("working now")
res = llm.predict(input)
print(res)
