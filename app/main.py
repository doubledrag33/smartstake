from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import auth, bets, ocr, database, models

# crea tutte le tabelle
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SmartStake API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# monta i router
app.include_router(auth.router)
app.include_router(bets.router)
app.include_router(ocr.router)

@app.get("/")
def read_root():
    return {"status": "SmartStake backend attivo"}
