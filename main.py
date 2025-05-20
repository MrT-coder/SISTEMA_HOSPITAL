from database import init_db
from services.registro_service import (
    registrar_servicio,
    registrar_producto,
    listar_cuentas,
    crear_cuenta
)
from services.factura_service import generar_factura
from services.paciente_service import registrar_paciente

def menu():
    while True:
        print("\n--- Sistema Hospitalario ---")
        print("1. Registrar Servicio Médico")
        print("2. Registrar Producto/Medicamento")
        print("3. Generar Factura")
        print("4. Crear Nueva Cuenta")
        print("5. Listar Cuentas")
        print("6. Registrar Paciente")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_cuentas()
            cuenta_id = int(input("ID de cuenta: "))
            tipo = input("Tipo de servicio: ")
            desc = input("Descripción: ")
            costo = float(input("Costo: "))
            registrar_servicio(cuenta_id, tipo, desc, costo)

        elif opcion == "2":
            listar_cuentas()
            cuenta_id = int(input("ID de cuenta: "))
            nombre = input("Nombre del producto: ")
            desc = input("Descripción: ")
            precio = float(input("Precio: "))
            registrar_producto(cuenta_id, nombre, desc, precio)

        elif opcion == "3":
            cuenta_id = int(input("ID de cuenta: "))
            factura = generar_factura(cuenta_id)
            if factura:
                print(f"Factura Generada ID: {factura['factura_id']}, Total: {factura['total']}, Fecha: {factura['fecha']}")
                paciente = factura['paciente']
                print(f"Paciente: {paciente['nombre']} (Cédula: {paciente['cedula']}, Estado: {paciente['estado']})")
            else:
                print("No se encontró una cuenta con ese ID.")

        elif opcion == "4":
            crear_cuenta()

        elif opcion == "5":
            listar_cuentas()
        
        elif opcion == "6":
            nombre = input("Nombre del paciente: ")
            cedula = input("Cédula del paciente: ")
            paciente, cuenta = registrar_paciente(nombre, cedula)
            print(f"✅ Paciente registrado con ID {paciente.id} y cuenta ID {cuenta.id}")

        elif opcion == "7":
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    init_db()
    menu()
