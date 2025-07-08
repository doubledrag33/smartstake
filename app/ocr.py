from fastapi import APIRouter, UploadFile, File
from PIL import Image
import pytesseract
import io

router = APIRouter(prefix="/ocr", tags=["ocr"])

@router.post("/")
async def extract_text(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    text = pytesseract.image_to_string(image)
    return {"text": text}