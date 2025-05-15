from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base

class Cuenta(Base):
    __tablename__ = 'cuentas'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    paciente = relationship("Paciente")

    total = Column(Float, default=0.0)
