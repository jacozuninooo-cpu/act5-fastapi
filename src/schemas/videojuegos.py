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