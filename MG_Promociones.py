


import json
from pathlib import Path
from datetime import datetime

DIAS_SEMANA = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Define el archivo de promociones en descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "promociones_rotativas.json"
    return archivo

# Crear el archivo si no existe
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        with open(archivo, "w", encoding = "utf-8") as p:
            promociones = {
                "dia_actual": "Lunes",
                "productos_con_descuento_hoy": [],
                "productos_usados_en_ciclo": [],
                "descuento_porcentaje": 0.20
            }
            json.dump(promociones, p, indent = 4, ensure_ascii = False)

# Carga las promociones de los productos desde el archivo json y retorna una lista de nombres de productos con descuento del dia actual
def cargar_promociones(archivo):
    with open(archivo, "r", encoding = "utf-8") as p:
        return json.load(p)

# Guarda las promociones de los productos en el archivo json recibiendo una lista de nombres de productos con descuento del dia actual
def guardar_promociones(archivo, datos):
    with open(archivo, "w", encoding = "utf-8") as p:
        json.dump(datos, p, indent = 4, ensure_ascii = False)

# Retorna los nombres de los productos que tienen descuento del dia actual
# Aplicando la logica de rotacion diaria y reinicio del ciclo cuando se acaben los productos sin descuento
def obtener_descuentos_del_dia(archivo, productos_list):
    crear_archivo_si_no_existe(archivo)
    datos = cargar_promociones(archivo)
    dia_actual = DIAS_SEMANA[datetime.now().weekday()]
    # Si se cambia el dia, se actualizan los descuentos
    if datos.get("dia_actual") != dia_actual:
        datos["dia_actual"] = dia_actual
        # Valida cuales son los productos que no han tenido descuento en el ciclo actual
        nombres_productos = [p.nombre() for p in productos_list]
        productos_sin_descuento = [
            nombre for nombre in nombres_productos 
            if nombre not in datos["productos_usados_en_ciclo"]
        ]
        # Si no hay mas productos sin descuento, se reinicia el ciclo
        if len(productos_sin_descuento) < 5:
            datos["productos_usados_en_ciclo"] = []
            productos_sin_descuento = nombres_productos[:]
        # Seleccionar los primeros 5 productos sin descuento para el dia actual 
        # Y agregarlos a la lista de productos con descuento del dia
        productos_hoy = productos_sin_descuento[:5]
        datos["productos_con_descuento_hoy"] = []
        for nombre in productos_hoy:
            for producto in productos_list:
                if producto.nombre() == nombre:
                    datos["productos_con_descuento_hoy"].append({
                        "nombre": nombre,
                        "precio": producto.precio(),
                        "descuento": "20%"
                    })
                    break
        # Agrega estos 5 productos a la lista de productos usados en el ciclo
        # para evitar que tengan descuento nuevamente hasta que se reinicie el ciclo
        datos["productos_usados_en_ciclo"].extend(productos_hoy)
        guardar_promociones(archivo, datos)
    # Retorna solo los nombres para aplicar los descuentos
    return [p["nombre"] for p in datos["productos_con_descuento_hoy"]]



