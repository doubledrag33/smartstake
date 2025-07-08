from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return JSONResponse(content={"text": text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
