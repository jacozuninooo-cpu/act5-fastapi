from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.juegos_models import VideoJuegoModel
from src.schemas.videojuegos import VideoJuego, VideoJuegoCreate

router = APIRouter(prefix="/videojuegos", tags=["Videojuegos"])

VideojuegoId = Annotated[int, Path(gt=0)]


@router.get("/", response_model=list[VideoJuego])
def obtener_videojuegos(db: Session = Depends(get_db)):
  videojuegos = db.query(VideoJuegoModel).all()
  return videojuegos


@router.get(
    "/{id}",
    response_model=VideoJuego,
    responses={404: {"description": "Videojuego no encontrado"}},
)
def obtener_videojuego_id(id: VideojuegoId, db: Session = Depends(get_db)):
  videojuego = (
      db.query(VideoJuegoModel).filter(VideoJuegoModel.id == id).first()
  )
  if not videojuego:
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")
  return videojuego


@router.post("/", response_model=VideoJuego, status_code=201)
def crear_videojuego(
    videojuego: VideoJuegoCreate, db: Session = Depends(get_db)
):
  nuevo_videojuego = VideoJuegoModel(**videojuego.model_dump())
  db.add(nuevo_videojuego)
  db.commit()
  db.refresh(nuevo_videojuego)
  return nuevo_videojuego


@router.put(
    "/{id}",
    response_model=VideoJuego,
    responses={404: {"description": "Videojuego no encontrado"}},
)
def actualizar_videojuego(
    id: VideojuegoId,
    videojuego_actualizado: VideoJuegoCreate = Body(),
    db: Session = Depends(get_db),
):
  videojuego = (
      db.query(VideoJuegoModel).filter(VideoJuegoModel.id == id).first()
  )
  if not videojuego:
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")

  for key, value in videojuego_actualizado.model_dump().items():
    setattr(videojuego, key, value)

  db.commit()
  db.refresh(videojuego)
  return videojuego


@router.delete(
    "/{id}",
    response_model=VideoJuego,
    responses={404: {"description": "Videojuego no encontrado"}},
)
def eliminar_videojuego(id: VideojuegoId, db: Session = Depends(get_db)):
  videojuego = (
      db.query(VideoJuegoModel).filter(VideoJuegoModel.id == id).first()
  )
  if not videojuego:
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")

  db.delete(videojuego)
  db.commit()
  return videojuego