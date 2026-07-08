from fastapi import FastAPI
import asyncio
from sse_starlette import EventSourceResponse, ServerSentEvent
from pydantic import BaseModel
import json
from services.loadingService import loading_service
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

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
    return EventSourceResponse(stream_chat(payload.content))

@app.post("/upload", response_class=EventSourceResponse)
def upload(payload: str):
    if not payload:
        return {"message": "No file uploaded."}
    loading_service(payload)
    return {"message": "Upload is  done."}