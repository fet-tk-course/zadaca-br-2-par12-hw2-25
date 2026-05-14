from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List, Optional

from models_a import Director
from models_b import Movie, MovieCreate, MovieUpdate
from database import get_session

router = APIRouter(prefix="/movies", tags=["Movies - Student_B"])

# GET /movies - lista svih filmova sa query filterom po godini
@router.get("/", response_model=List[Movie])
def read_movies(year: Optional[int] = None, session: Session = Depends(get_session)):
    query = select(Movie)
    if year is not None:
        query = query.where(Movie.year == year)
    movies = session.exec(query).all()
    count = len(movies)
    return movies




@router.get("/statistics", response_model=dict)
def statistics_movies(rating: float, session: Session = Depends(get_session)):

    query=select(Movie).where(Movie.rating>rating)
    movies=session.exec(query).all()
    count=len(movies)
    average_rating=sum(movie.rating for movie in movies) / count

    return avarage_rating
  
  



# GET /movies/{id} - za dohvatanje filma preko njegovog ID-a ako film ne postoji vraca 404
@router.get("/{id}", response_model=Movie)
def read_movie(id: int, session: Session = Depends(get_session)):
    movie = session.get(Movie, id)
    if not movie:
        raise HTTPException(status_code=404, detail="Film nije pronađen")
    return movie

@router.get("/",response_model=Movie)


#POST /movies - za kreiranje novog filma (Status 201)
@router.post("/", response_model=Movie, status_code=201)
def create_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    if movie.director_id is not None:
        # Provjera da li direktor postoji
        director = session.get(Director, movie.director_id)
        if not director:
            raise HTTPException(status_code=400, detail="Reziser sa datim ID-om ne postoji")
    if movie.title == title:
        raise HTTPException(status_code=409, detail="Film sa datim nazivom vec postoji")
   


    new_movie = Movie.from_orm(movie)
    session.add(new_movie)
    session.commit()
    session.refresh(new_movie)
    return new_movie


# PUT /movies/{id} - potpuna zamjena filma (ako film ne postoji vraca 404)
@router.put("/{id}", response_model=Movie)
def update_movie(id: int, movie_data: MovieCreate, session: Session = Depends(get_session)):
    db_movie = session.get(Movie, id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Film nije pronađen")
    
    if movie_data.director_id is not None:
        # Provjera da li direktor postoji
        director = session.get(Director, movie_data.director_id)
        if not director:
            raise HTTPException(status_code=400, detail="Reziser sa datim ID-om ne postoji")

    for key, value in movie_data.dict().items():
        setattr(db_movie, key, value)
    
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)
    return db_movie


# PATCH /movies/{id} - djelimicno azuriranje (exclude_unset=True)
@router.patch("/{id}", response_model=Movie)
def patch_movie(id: int, movie_update: MovieUpdate, session: Session = Depends(get_session)):
    movie = session.get(Movie, id)
    if not movie:
        raise HTTPException(status_code=404, detail="Film nije pronađen")
    
    if movie_update.director_id is not None:
        # Provjera da li direktor postoji
        director = session.get(Director, movie_update.director_id)
        if not director:
            raise HTTPException(status_code=400, detail="Reziser sa datim ID-om ne postoji")
    
    update_data = movie_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(movie, key, value)
    
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie


# DELETE /movies/{id} - za brisanje filma iz baze(Status 204)
@router.delete("/{id}", status_code=204)
def delete_movie(id: int, session: Session = Depends(get_session)):
    movie = session.get(Movie, id)
    if not movie:
        raise HTTPException(status_code=404, detail="Film nije pronađen")
    
    session.delete(movie)
    session.commit()
    return None


