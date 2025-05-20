from models.paciente import Paciente
from models.cuenta import Cuenta
from database import Session

def registrar_paciente(nombre, cedula):
    with Session() as session:
        paciente = Paciente(nombre=nombre, cedula=cedula, estado='hospitalizado')
        session.add(paciente)
        session.commit()
        session.refresh(paciente)  # Obligamos a que traiga el ID

        cuenta = Cuenta(paciente_id=paciente.id, total=0.0)
        session.add(cuenta)
        session.commit()
        session.refresh(cuenta)  # Igual para la cuenta

        # Accedemos a los valores ANTES de salir del contexto
        paciente_id = paciente.id
        cuenta_id = cuenta.id

        # Devolvemos los objetos con los datos ya accedidos
        return paciente, cuenta
