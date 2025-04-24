from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Allow all CORS for testing purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract_requirements")
async def extract_requirements(file: UploadFile = File(...)):
    # Simulated requirement extraction logic
    return {
        "filename": file.filename,
        "requirements": [
            "Locate underground power lines",
            "Scan site with GPR",
            "Submit utility map within 48 hours"
        ]
    }