from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio_unitario = Column(Float)
