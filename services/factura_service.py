from database import Session
from models.factura import Factura
from models.cuenta import Cuenta

def generar_factura(cuenta_id):
    with Session() as session:
        cuenta = session.query(Cuenta).get(cuenta_id)
        if not cuenta:
            return None

        factura = Factura(cuenta_id=cuenta.id, total=cuenta.total)
        session.add(factura)
        session.commit()

        # Accede a los valores ANTES de cerrar la sesión
        factura_id = factura.id
        factura_total = factura.total

        return {"id": factura_id, "total": factura_total}