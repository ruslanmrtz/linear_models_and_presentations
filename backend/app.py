from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from .models import Member, Booking, Facility
from .config import SessionLocal
from .schemas import UserRegister, UserGet, BookingGet

app = FastAPI()


def get_session():
    with SessionLocal() as session:
        return session


@app.get('/users/all', response_model=List[UserGet])
def get_users(limit: int = 8, db: Session = Depends(get_session)):
    return db.query(Member).limit(limit).all()


@app.get('/bookings/all', response_model=List[BookingGet])
def get_bookings(limit: int = 8, db: Session = Depends(get_session)):
    return db.query(Booking).limit(limit).all()


@app.get('/facilities/all')
def get_facilities(limit: int = 8, db: Session = Depends(get_session)):
    return db.query(Facility).limit(limit).all()







