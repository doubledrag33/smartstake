from pydantic import BaseModel
from typing import List
from datetime import datetime

# --- Bet DTOs ---
class BetBase(BaseModel):
    event: str
    odds: float
    stake: float
    result: str

class BetCreate(BetBase):
    pass

class BetRead(BetBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# --- User DTOs ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    bets: List[BetRead] = []

    class Config:
        orm_mode = True
