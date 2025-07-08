from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Bet(Base):
    __tablename__ = "bets"
    id = Column(Integer, primary_key=True, index=True)
    event = Column(String)
    quota = Column(Float)
    stake = Column(Float)
    esito = Column(String)