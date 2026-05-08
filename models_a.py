from sqlmodel import SQLModel, Field
from typing import Optional

# TODO: Student A - Definiši svoj SQLModel entitet ovdje

class Director(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    nationality: str
    birth_year: int
    awards: int
    active:bool
    rating: float

class DirectorCreate(SQLModel):
    name: str
    nationality: str
    birth_year: int
    awards: int
    active: bool
    rating: float

class DirectorUpdate(SQLModel):
    name: Optional[str] = None
    nationality: Optional[str] = None
    birth_year: Optional[int] = None    
    awards: Optional[int] = None
    active: Optional[bool] = None
    rating: Optional[float] = None