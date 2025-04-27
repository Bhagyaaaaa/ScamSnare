# main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/check")
async def check_media(file: UploadFile = File(None), link: str = Form(None)):
    if file:
        contents = await file.read()
        print(f"Received file of size: {len(contents)} bytes")
        # Here you can add real detection code later
        result = random.choice(["Real", "Fake"])
        return JSONResponse(content={"result": result})

    if link:
        print(f"Received link/text: {link}")
        # Simple fake check for demo
        if "free money" in link.lower() or "lottery" in link.lower():
            result = "Fake"
        else:
            result = random.choice(["Real", "Fake"])
        return JSONResponse(content={"result": result})

    return JSONResponse(content={"error": "No file or link provided."}, status_code=400)
