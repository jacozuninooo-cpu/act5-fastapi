from src.database import Base
from sqlalchemy import Column, Integer, String


class VideoJuegoModel(Base):
  __tablename__ = "videojuegos"

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  nombre = Column(String, index=True, nullable=False)
  genero = Column(String, nullable=False)
  puntuacion = Column(Integer, nullable=False)