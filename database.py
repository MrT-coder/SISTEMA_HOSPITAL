# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models import paciente, servicio, producto, cuenta, factura

# Crear el engine
engine = create_engine('sqlite:///hospital.db', echo=True)

# Crear una clase Session local
Session = sessionmaker(bind=engine)

# Función para inicializar la base de datos
def init_db():
    Base.metadata.create_all(engine)
    print("Base de datos hospital.db creada correctamente.")
