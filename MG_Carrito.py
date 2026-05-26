


import json
from pathlib import Path
from datetime import datetime


# Define el archivo de compras en descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "compras.json"
    return archivo


# Crea el archivo si no existe
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        with open(archivo, "w", encoding = "utf-8") as c:
            json.dump([], c)


# Carga las compras desde el archivo json y retorna una lista con los datos
def cargar_compras(archivo):
    crear_archivo_si_no_existe(archivo)
    with open(archivo, "r", encoding = "utf-8") as c:
        compras_data = json.load(c)
    return compras_data


# Guarda las compras en el archivo json, agregando una nueva compra al historial
def guardar_compra(archivo, carrito, usuario = None):
    compras = cargar_compras(archivo)
    # Crea los datos de la compra con la informacion del carrito y el usuario (si esta logueado)
    productos_comprados = []
    for item in carrito.productos():
        productos_comprados.append({
            "nombre": item.nombre(),
            "precio": item.precio(),
            "cantidad": item.cantidad(),
            "subtotal": item.precio() * item.cantidad()
        })
    compra = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": usuario.nombre() if usuario else "Desconocido",
        "productos": productos_comprados,
        "total": carrito.calcular_total()
    }
    compras.append(compra)
    with open(archivo, "w", encoding = "utf-8") as c:
        json.dump(compras, c, indent = 4, ensure_ascii = False)


# Muestra el historial de compras
def mostrar_compras(archivo):
    compras = cargar_compras(archivo)
    if not compras:
        print("No hay compras registradas.")
        return
    print("\n---- Historial de Compras ----")
    for i, compra in enumerate(compras, 1):
        print(f"\nCompra #{i}")
        print(f"Fecha: {compra["fecha"]}")
        print(f"Usuario: {compra["usuario"]}")
        print("Productos:")
        for producto in compra["productos"]:
            print(f"  - {producto["nombre"]} x{producto["cantidad"]} - ${producto["precio"]} - Subtotal: ${producto["subtotal"]}")
        print(f"Total: ${compra["total"]}")



