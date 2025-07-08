from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Bet
from app.database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/bets", tags=["bets"])

class BetIn(BaseModel):
    event: str
    quota: float
    stake: float
    esito: str

@router.post("/")
def create_bet(bet: BetIn, db: Session = Depends(get_db)):
    new_bet = Bet(**bet.dict())
    db.add(new_bet)
    db.commit()
    return {"message": "Bet saved"}

@router.get("/", response_model=List[BetIn])
def get_bets(db: Session = Depends(get_db)):
    return db.query(Bet).all()