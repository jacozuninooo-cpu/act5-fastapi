from typing import Annotated
from pydantic import BaseModel, Field


class VideoJuegoCreate(BaseModel):
  nombre: Annotated[
      str, Field(min_length=1, description="Nombre del videojuego")
  ]
  genero: Annotated[str, Field(min_length=1, description="Genero del videojuego")]
  puntuacion: Annotated[
      int, Field(ge=0, le=10, description="Puntuacion del videojuego")
  ]


class VideoJuego(VideoJuegoCreate):
  id: Annotated[int, Field(gt=0, description="ID del videojuego")]

  class Config:
    from_attributes = True 

from typing import Optional
from sqlmodel import SQLModel

class EstudioCreate(SQLModel):
  nombre: str
  pais: str

class EstudioRead(EstudioCreate):
  id: int

class VideoJuegoCreate(SQLModel):
  nombre: str
  genero: str
  puntuacion: int
  estudio_id: Optional[int] = None

class VideoJuegoReadWithEstudio(SQLModel):
  id: int
  nombre: str
  genero: str
  puntuacion: int
  estudio: Optional[EstudioRead] = None  # ¡Dato anidado!