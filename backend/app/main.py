from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CareerPathAI backend is running 🚀"}
