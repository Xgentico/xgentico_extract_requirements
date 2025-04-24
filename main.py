from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract_requirements")
async def extract_requirements(file: UploadFile = File(...)):
    contents = await file.read()
    extracted_reqs = []

    try:
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

            for line in full_text.splitlines():
                if re.search(r"\b(shall|must|required|submit|provide|mark|include)\b", line, re.IGNORECASE):
                    extracted_reqs.append(line.strip())

    except Exception as e:
        return {"error": str(e)}

    return {
        "filename": file.filename,
        "requirements": extracted_reqs
    }