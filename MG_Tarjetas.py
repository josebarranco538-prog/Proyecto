


import json
from pathlib import Path


# Define el archivo de tarjetas en descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "tarjetas.json"
    return archivo


# Crea el archivo si no existe y lo inicializa con un diccionario vacio
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        with open(archivo, "w", encoding = "utf-8") as t:
            json.dump({}, t)


# Carga los datos de tarjeta del usuario
def cargar_datos_tarjeta(archivo, usuario):
    with open(archivo, "r", encoding = "utf-8") as t:
        tarjetas = json.load(t)
    return tarjetas.get(usuario)


# Guarda los datos de tarjeta del usuario en el archivo, asignando un saldo inicial de 1 millon si no existe
# Valida que el CVC no sea de una tarjeta diferente
def guardar_datos_tarjeta(archivo, usuario, numero_tarjeta, cvc):
    with open(archivo, "r", encoding = "utf-8") as t:
        tarjetas = json.load(t)
    
    # Validar que el CVC sea numerico y tenga 3 digitos
    if not cvc.isdigit() or len(cvc) != 3:
        print("Error: CVC invalido. Debe tener 3 digitos numericos.")
        return False
    
    # Validar que el CVC no pertenezca a otra tarjeta de otro usuario
    for otro_usuario, datos in tarjetas.items():
        if otro_usuario != usuario:
            if datos.get("numero_tarjeta") != numero_tarjeta and datos.get("cvc") == cvc:
                print("Error: Este CVC no es de esta tarjeta.")
                return False
    
    tarjetas[usuario] = {"numero_tarjeta": numero_tarjeta, "cvc": cvc, "saldo": 1_000_000}
    with open(archivo, "w", encoding = "utf-8") as t:
        json.dump(tarjetas, t, indent = 4)
    return True


# Verifica si hay saldo suficiente en la tarjeta del usuario para realizar una compra por el monto especificado
def verificar_saldo(archivo, usuario, monto):
    with open(archivo, "r", encoding = "utf-8") as t:
        tarjetas = json.load(t)
    datos_tarjeta = tarjetas.get(usuario)
    if datos_tarjeta:
        # asigna el saldo inicial
        if "saldo" not in datos_tarjeta:
            datos_tarjeta["saldo"] = 1_000_000
            tarjetas[usuario] = datos_tarjeta
            with open(archivo, "w", encoding = "utf-8") as t:
                json.dump(tarjetas, t, indent = 4)
        return datos_tarjeta["saldo"] >= monto
    return False


# Descuenta el saldo de la tarjeta del usuario por el monto especificado despues de una compra exitosa
def descontar_saldo(archivo, usuario, monto):
    with open(archivo, "r", encoding = "utf-8") as t:
        tarjetas = json.load(t)
    datos_tarjeta = tarjetas.get(usuario)
    if datos_tarjeta and "saldo" in datos_tarjeta:
        datos_tarjeta["saldo"] -= monto
        tarjetas[usuario] = datos_tarjeta
        with open(archivo, "w", encoding = "utf-8") as t:
            json.dump(tarjetas, t, indent = 4)




