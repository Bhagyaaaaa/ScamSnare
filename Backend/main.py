# main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random
import os

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
        file_size = len(contents)
        print(f"Received file of size: {file_size} bytes, filename: {file.filename}")

        # Here you can add real image/video fake detection code later.
        # For now, we simulate based on file size (just for demo):
        if file_size < 50000:  # small files are fake (demo logic)
            result = "Fake"
        else:
            result = "Real"

        return JSONResponse(content={"result": result})

    if link:
        print(f"Received link/text: {link}")

        # Simple fake check for demo (you can replace with real logic later)
        suspicious_keywords = ["free money", "lottery", "100% guaranteed", "win big"]
        if any(keyword in link.lower() for keyword in suspicious_keywords):
            result = "Fake"
        else:
            result = random.choice(["Real", "Fake"])  # random if not sure

        return JSONResponse(content={"result": result})

    return JSONResponse(content={"error": "No file or link provided."}, status_code=400)
