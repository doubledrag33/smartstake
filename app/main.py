from fastapi import FastAPI
from app import auth, bets, ocr  # importa i router separati
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS: richieste da frontend esterni (Next.js ecc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in produzione: metti solo il dominio frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint test base
@app.get("/")
def read_root():
    return {"message": "SmartStake backend è attivo"}

# Includi tutte le route modulari
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(bets.router, prefix="/bets", tags=["bets"])
app.include_router(ocr.router, prefix="/ocr", tags=["ocr"])
