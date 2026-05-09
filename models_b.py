from sqlmodel import SQLModel, Field
from typing import Optional

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
class MovieCreate(SQLModel):
    title: str
    year: int
    rating: float
    is_oscar_winner: bool
    description: Optional[str] = None

class MovieUpdate(SQLModel):
    title: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    is_oscar_winner: Optional[bool] = None
    description: Optional[str] = None

