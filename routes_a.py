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

#Dohvatanje statistike - prosječna ocjena svih režisera
@router.get("/statistics")
def get_statistics(session: Session = Depends(get_session)):
    directors=session.get(Director).all()
    if not directors:
        return {"Prosjek rejtinga":0}
    average_rating = sum(d.rating for d in directors)/len(directors)
    return {"Prosjek rejtinga": average_rating}

# Dohvatanje jednog režisera po ID-u
@router.get("/{director_id}")
def get_director(director_id: int, session: Session = Depends(get_session)):
    director = session.get(Director, director_id)
    if not director:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Režiser nije pronađen")
    return director

# Kreiranje novog režisera
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_director(director: DirectorCreate, session: Session = Depends(get_session)):

    existing=session.exec(select(Director).where(Director.name==director.name)).first()

    if existing:
        raise HTTPException(status_code=409 detail="Režiser sa ovim imenom već postoji")
    
    new_director = Director.model_validate(director)    
    session.add(new_director)
    session.commit()
    session.refresh(new_director)
    return new_director


# Potpuna zamjena režisera
@router.put("/{director_id}")
def update_director(director_id: int, director_update: DirectorCreate, session: Session = Depends(get_session)):
    existing = session.get(Director, director_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Režiser nije pronađen")
    
    director_data = director_update.model_dump()
    for key, value in director_data.items():
        setattr(existing, key, value)

    session.add(existing)
    session.commit()
    session.refresh(existing)
    return existing

# Djelimično ažuriranje režisera
@router.patch("/{director_id}")
def patch_director(director_id: int, director_update: DirectorUpdate, session:Session = Depends(get_session)):
    existing = session.get(Director, director_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Režiser nije pronađen")
    
    update_data = director_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing, key, value)

    session.add(existing)

    session.commit()
    session.refresh(existing)
    return existing

# Brisanje režisera
@router.delete("/{director_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_director(director_id: int, session: Session = Depends(get_session)):
    existing = session.get(Director, director_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Režiser nije pronađen")
    
    session.delete(existing)
    session.commit()