from sqlalchemy import create_engine
from models import Base

# Crear motor SQLite
engine = create_engine('sqlite:///hospital.db')

# Crear todas las tablas definidas en los modelos
Base.metadata.create_all(engine)

print("Base de datos 'hospital.db' creada con éxito.")
