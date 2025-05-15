from database import Session
from models.servicio import Servicio
from models.producto import Producto
from models.cuenta import Cuenta

# Registrar un servicio
def registrar_servicio(cuenta_id, tipo, descripcion, costo):
    with Session() as session:
        cuenta = session.query(Cuenta).get(cuenta_id)
        if cuenta is None:
            print(f"❌ Cuenta con ID {cuenta_id} no existe.")
            return
        servicio = Servicio(tipo=tipo, descripcion=descripcion, costo=costo)
        session.add(servicio)
        cuenta.total += costo
        session.commit()
        print("✅ Servicio registrado y cuenta actualizada.")

# Registrar un producto
def registrar_producto(cuenta_id, nombre, descripcion, precio):
    with Session() as session:
        cuenta = session.query(Cuenta).get(cuenta_id)
        if cuenta is None:
            print(f"❌ Cuenta con ID {cuenta_id} no existe.")
            return
        producto = Producto(nombre=nombre, descripcion=descripcion, precio_unitario=precio)
        session.add(producto)
        cuenta.total += precio
        session.commit()
        print("✅ Producto registrado y cuenta actualizada.")

# Listar cuentas existentes
def listar_cuentas():
    with Session() as session:
        cuentas = session.query(Cuenta).all()
        if not cuentas:
            print("⚠️ No hay cuentas registradas.")
            return
        print("\n📋 Cuentas disponibles:")
        for cuenta in cuentas:
            print(f"ID: {cuenta.id} - Total: {cuenta.total}")

# Crear una nueva cuenta
def crear_cuenta():
    with Session() as session:
        nueva_cuenta = Cuenta(total=0.0)
        session.add(nueva_cuenta)
        session.commit()
        print(f"✅ Cuenta creada exitosamente con ID: {nueva_cuenta.id}")
