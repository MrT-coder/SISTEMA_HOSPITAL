from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime

class Factura(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    cuenta_id = Column(Integer, ForeignKey('cuentas.id'))
    cuenta = relationship("Cuenta")
    total = Column(Float)
    fecha = Column(DateTime, default=datetime.utcnow)
