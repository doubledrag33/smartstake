from fastapi import FastAPI
from app import auth, ocr, bets
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(ocr.router)
app.include_router(bets.router)

@app.get("/")
def root():
    return {"message": "SmartStake backend attivo con DB"}