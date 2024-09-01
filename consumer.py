from fastapi import FastAPI, HTTPException
import requests
import os
import time
import threading
app = FastAPI()

BROKER_URL = os.getenv("BROKER_URL", "http://127.0.0.1:8000")
TOPIC = os.getenv("TOPIC", "tasks")


def consume_message():
    try:
        print("Attempting to consume message...")
        response = requests.get(f"{BROKER_URL}/consume/{TOPIC}")
        response.raise_for_status()  # Verifica si ocurrió un error HTTP
        message = response.json()
        print(f"Consumed message: {message['message']}")

        # Acknowledge the message after processing
        ack_response = requests.post(f"{BROKER_URL}/acknowledge/{TOPIC}",
                                     json={"topic": TOPIC, "message_id": message["id"]})
        ack_response.raise_for_status()
        print(f"Acknowledged message ID: {message['id']}")
        return {"status": "success", "message": message['message']}
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"status": "no_message", "detail": f"No messages available in topic '{TOPIC}'"}
        else:
            print(f"Error consuming message: {e}")
            return {"status": "error", "detail": str(e)}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


@app.post("/trigger-consume/")
async def trigger_consume():
    result = consume_message()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["detail"])
    return result

def start_consumer():
    while True:
        print("Consumer running...")
        consume_message()
        time.sleep(60)


if __name__ == "__main__":
    import uvicorn

    consume_thread = threading.Thread(target=start_consumer, daemon=True)
    consume_thread.start()

    uvicorn.run(app, host="0.0.0.0", port=8002)
