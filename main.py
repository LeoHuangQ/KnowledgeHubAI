import asyncio
import json

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from sse_starlette import EventSourceResponse, ServerSentEvent

load_dotenv(dotenv_path=".env")

from services.loadingService import loading_service
from services.ragService import rag_service

app = FastAPI()

class MessagePayload(BaseModel):
    id: int
    content: str

@app.get("/health")
def healthCheck():
    return {'status':'Server is running!'}

async def stream_chat(inputData: str):
    for i in range(len(inputData)):
        token = inputData[i]
        # print(token)
        yield ServerSentEvent(
            event = "message",
            data=json.dumps({"text":token}))
        await asyncio.sleep(0.1)
    yield ServerSentEvent(
        event="end",
        data="done"
    )

@app.post("/chatbot", response_class=EventSourceResponse)
async def chatbot(payload: MessagePayload):
    return EventSourceResponse(rag_service(payload.content))

@app.post("/upload", response_class=EventSourceResponse)
def upload(payload: str):
    if not payload:
        return {"message": "No file uploaded."}
    loading_service(payload)
    return {"message": "Upload is  done."}