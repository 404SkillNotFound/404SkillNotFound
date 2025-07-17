from fastapi import FastAPI, Request
from chatbot import get_chat_response


app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("message")
    if not query:
        return {"error": "No message provided"}
    answer = get_chat_response(query)
    return {"response": answer}
