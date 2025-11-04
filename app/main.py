from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from Python + DevOps + Render 🚀",
        "timestamp": datetime.utcnow().isoformat()
    }
