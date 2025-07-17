from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, schemas, auth

router = APIRouter(prefix="/bets", tags=["bets"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BetRead)
def create_bet(
    bet_in: schemas.BetCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    bet = models.Bet(**bet_in.dict(), user_id=current_user.id)
    db.add(bet)
    db.commit()
    db.refresh(bet)
    return bet

@router.get("/", response_model=list[schemas.BetRead])
def list_bets(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(models.Bet).filter(models.Bet.user_id == current_user.id).all()
