from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract, io

router = APIRouter(tags=["ocr"])

@router.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Il file deve essere un'immagine")
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nell'OCR: {e}")
