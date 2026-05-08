from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from database import get_session
from models_a import Director, DirectorCreate, DirectorUpdate

router = APIRouter(prefix="/directors", tags=["Directors"])

# Dohvatanje liste svih reditelja (sa opcionalnim filterom po nacionalnosti)
@router.get("/")
def get_directors(
    nationality:Optional[str]=Query(default=None),
    session: Session = Depends(get_session)
    ):
    query = select(Director)

    if nationality:
        query = query.where(Director.nationality==nationality)

    directors = session.exec(query).all()
    return directors

@router.get("/{director_id}")
def get_director(director_id: int, session: Session = Depends(get_session)):
    director = session.get(Director, director_id)
    if not director:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reditelj nije pronađen")
    return director