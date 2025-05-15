from database import Session
from models.factura import Factura
from models.cuenta import Cuenta

def generar_factura(paciente_id):
    with Session() as session:
        cuenta = session.query(Cuenta).filter_by(paciente_id=paciente_id).first()
        factura = Factura(cuenta_id=cuenta.id, total=cuenta.total)
        session.add(factura)
        session.commit()
        return factura
