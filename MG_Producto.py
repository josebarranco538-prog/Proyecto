


import json
from pathlib import Path
from Producto import Producto


# Definir archivo en Descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "productos.json"
    return archivo


# Crear archivo si no existe
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        with open(archivo, "w", encoding = "utf-8") as p:
            json.dump([], p)


# Cargar productos
def cargar_productos(archivo):
    crear_archivo_si_no_existe(archivo)
    
    with open(archivo, "r", encoding = "utf-8") as p:
        productos_data = json.load(p)
    
    productos = []
    for p in productos_data:
        producto = Producto(p["nombre"], p["precio"], p.get("stock", 0))
        productos.append(producto)
    
    return productos


# Guardar productos
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



