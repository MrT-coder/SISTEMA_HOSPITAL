from datetime import datetime
from models.factura import Factura
from models.cuenta import Cuenta
from models.paciente import Paciente
from database import Session

def generar_factura(cuenta_id):
    with Session() as session:
        cuenta = session.query(Cuenta).get(cuenta_id)
        if not cuenta:
            print(f"No se encontró la cuenta con ID {cuenta_id}.")
            return None

        paciente = session.query(Paciente).get(cuenta.paciente_id)

        factura = Factura(cuenta_id=cuenta.id, total=cuenta.total, fecha=datetime.now())
        session.add(factura)
        session.commit()

        return {
            "factura_id": factura.id,
            "total": factura.total,
            "fecha": factura.fecha,
            "paciente": {
                "id": paciente.id,
                "nombre": paciente.nombre,
                "cedula": paciente.cedula,
                "estado": paciente.estado
            }
        }
