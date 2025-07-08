from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import io

app = FastAPI()

# CORS per permettere richieste dal frontend (Next.js su Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione meglio specificare il dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "SmartStake backend attivo"}

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Il file deve essere un'immagine")

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)

        return {
            "text": text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore nell'elaborazione dell'immagine: {str(e)}")
