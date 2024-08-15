from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional
from pydantic import BaseModel
import uuid

app = FastAPI()


class Event:
    def __init__(self, content: str):
        self.id = str(uuid.uuid4())
        self.content = content
        self.processed = False


class MessageBroker:
    def __init__(self):
        self.topics: Dict[str, List[Event]] = {}

    def add_event(self, topic: str, content: str) -> str:
        if topic not in self.topics:
            self.topics[topic] = []
        event = Event(content)
        self.topics[topic].append(event)
        return event.id

    def get_event(self, topic: str) -> Optional[Event]:
        if topic not in self.topics or not self.topics[topic]:
            return None
        for message in self.topics[topic]:
            if not message.processed:
                message.processed = True
                return message
        return None

    def acknowledge_event(self, topic: str, message_id: str) -> bool:
        if topic not in self.topics:
            return False
        for message in self.topics[topic]:
            if message.id == message_id and message.processed:
                self.topics[topic].remove(message)
                return True
        return False

    def list_events(self, topic: str) -> Optional[List[Dict]]:
        if topic not in self.topics:
            return None
        return [{"id": msg.id, "content": msg.content, "processed": msg.processed} for msg in self.topics[topic]]


broker = MessageBroker()


class MessageInput(BaseModel):
    topic: str
    content: str


@app.post("/produce/")
async def produce(message: MessageInput):
    message_id = broker.add_event(message.topic, message.content)
    return {"status": f"Message added to the topic '{message.topic}'", "id": message_id}


@app.get("/consume/{topic}")
async def consume(topic: str):
    message = broker.get_event(topic)
    if not message:
        raise HTTPException(status_code=404, detail="No messages in the topic")
    return {"id": message.id, "message": message.content}


class AcknowledgeInput(BaseModel):
    topic: str
    message_id: str


@app.post("/acknowledge/{topic}")
async def acknowledge(message: AcknowledgeInput):
    acknowledged = broker.acknowledge_event(message.topic, message.message_id)
    if not acknowledged:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"status": "Message acknowledged"}


@app.get("/list/{topic}")
async def list_messages(topic: str):
    messages = broker.list_events(topic)
    if messages is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {"topic": topic, "messages": messages}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
