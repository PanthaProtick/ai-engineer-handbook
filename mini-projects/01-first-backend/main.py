import fastapi

app=fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


#uv run uvicorn main:app --host 127.0.0.1 --port 8000 --reload