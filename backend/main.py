from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import agent_reply
from tools import send_email, send_sms, web_search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(q: Query):
    reply = agent_reply(q.message)
    return {"response": reply}

@app.post("/email")
def email(data: dict):
    return {"status": send_email(data["to"], data["subject"], data["message"])}

@app.post("/sms")
def sms(data: dict):
    return {"status": send_sms(data["number"], data["text"])}

@app.get("/search")
def search(q: str):
    return {"result": web_search(q)}

