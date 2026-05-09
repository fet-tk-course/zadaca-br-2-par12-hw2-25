from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models_a import Director

# TODO: Student B - Definiši svoj SQLModel entitet ovdje
# 
class Movie(SQLModel, table=True):
    #automatski generisani ID
    id: Optional[int] = Field(default=None, primary_key=True)
    #5 razlicith tipova (string,int,float,bool,optional)
    title: str 
    year: int
    rating: float
    is_oscar_winner: bool
    description: Optional[str] = Field(default=None, max_length=500)
    kolegica_id: Optional[int] = Field(default=None, foreign_key="director.id")
    kolegica: Optional[Director] = Relationship()
    
class MovieCreate(SQLModel):
    title: str
    year: int
    rating: float
    is_oscar_winner: bool
    description: Optional[str] = None
    kolegica_id: Optional[int] = None

class MovieUpdate(SQLModel):
    title: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    is_oscar_winner: Optional[bool] = None
    description: Optional[str] = None
    kolegica_id: Optional[int] = None
    
