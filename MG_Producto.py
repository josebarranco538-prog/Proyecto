


import json
from pathlib import Path
from Producto import Producto


# Define el archivo de productos en Descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "productos.json"
    return archivo


# Crea el archivo si no existe
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        with open(archivo, "w", encoding = "utf-8") as p:
            json.dump([], p)


# Carga los productos desde el archivo json y retorna una lista de objetos producto
def cargar_productos(archivo):
    crear_archivo_si_no_existe(archivo)
    with open(archivo, "r", encoding = "utf-8") as p:
        productos_data = json.load(p)
    productos = []
    for p in productos_data:
        producto = Producto(p["nombre"], p["precio"], p.get("stock", 0), p.get("descuento", 0))
        productos.append(producto)
    return productos


# Guarda los productos en el archivo json, convirtiendo los objetos producto a diccionarios
def guardar_productos(archivo, productos):
    productos_data = []
    for p in productos:
        productos_data.append({
            "nombre": p.nombre(),
            "precio": p.precio(),
            "stock": p.stock()
        })
    with open(archivo, "w", encoding = "utf-8") as p:
        json.dump(productos_data, p, indent = 4, ensure_ascii = False)



