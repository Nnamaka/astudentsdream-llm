from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"astudentsdream llm": "underconstruction 🚧"}

