from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from database import get_session
from models_a import Director, DirectorCreate, DirectorUpdate

router = APIRouter(prefix="/directors", tags=["Directors"])

# Dohvatanje liste svih režisera (sa opcionalnim filterom po nacionalnosti)
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

# Dohvatanje jednog režisera po ID-u
@router.get("/{director_id}")
def get_director(director_id: int, session: Session = Depends(get_session)):
    director = session.get(Director, director_id)
    if not director:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Režiser nije pronađen")
    return director

# Kreiranje novog reditelja
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_director(director: DirectorCreate, session: Session = Depends(get_session)):
    new_director = Director.model_validate(director)
    session.add(new_director)
    session.commit()
    session.refresh(new_director)
    return new_director