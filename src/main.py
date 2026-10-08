from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import SessionLocal, engine
from src.models.juegos_models import Base, VideoJuegoModel
from src.routers.videojuegos import router as videojuegos_router

Base.metadata.create_all(bind=engine)

def seed_videojuegos():
  db = SessionLocal()
  try:
    count = db.query(VideoJuegoModel).count()
    if count == 0:
      juegos_iniciales = [
          VideoJuegoModel(
              nombre="GTA V", genero="Mundo Abierto", puntuacion=10
          ),
          VideoJuegoModel(nombre="League of Legends", genero="MOBA", puntuacion=7),
          VideoJuegoModel(nombre="Call of Duty", genero="Disparos", puntuacion=8),
          VideoJuegoModel(nombre="Roblox", genero="MMO", puntuacion=4),
          VideoJuegoModel(nombre="Minecraft", genero="Sandbox", puntuacion=1),
      ]
      db.add_all(juegos_iniciales)
      db.commit()
      print("¡Juegos iniciales cargados con éxito!")
  finally:
    db.close()

seed_videojuegos()

app = FastAPI(title="API de Videojuegos - SQLAlchemy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(videojuegos_router)