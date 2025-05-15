from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)  # Ej: "atencion", "laboratorio", etc.
    descripcion = Column(String)
    costo = Column(Float)
