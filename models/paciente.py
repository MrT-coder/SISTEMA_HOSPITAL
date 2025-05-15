from sqlalchemy import Column, Integer, String
from models.base import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cedula = Column(String, unique=True)
    estado = Column(String)  # 'hospitalizado', 'alta'
