from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"msg": "V12 backend running"}

@app.get("/top")
def top():
    return [
        {"code": "2330", "name": "台積電", "score": 92},
        {"code": "2454", "name": "聯發科", "score": 88},
    ]
