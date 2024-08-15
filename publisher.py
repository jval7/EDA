from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

BROKER_URL = os.getenv("BROKER_URL", "http://127.0.0.1:8000/produce/")


class PublishMessage(BaseModel):
    topic: str
    content: str


@app.post("/publish/")
async def publish(message: PublishMessage):
    try:
        response = requests.post(BROKER_URL, json=message.dict())
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish message: {str(e)}")

    return {"status": "Message published", "broker_response": response.json()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
