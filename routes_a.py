from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from database import get_session
from models_a import Director, DirectorCreate, DirectorUpdate

router = APIRouter(prefix="/directors", tags=["Directors"])

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