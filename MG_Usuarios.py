


import json
from pathlib import Path


# Definir archivo en descargas
def definir_archivo():
    
    archivo = Path.home() / "Downloads" / "usuarios.json"
    print("Archivo se guardará en:", archivo)
    return archivo


# Crear archivo si no existe
def crear_archivo_si_no_existe(archivo):
    
    if not archivo.exists():
        print("Archivo no existe, creando uno nuevo...")
        with open(archivo, "w", encoding = "utf-8") as u:
            json.dump({}, u)
    else:
        print("Archivo ya existe")


# Cargar usuarios
def cargar_usuarios(archivo):
    
    with open(archivo, "r", encoding = "utf-8") as u:
        usuarios = json.load(u)
    return usuarios


# Registro
def registrar_usuario(archivo, usuarios):
    
    print("\n---- Registro ----")
    
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    
    if username in usuarios:
        print("Ese usuario ya existe")
    else:
        usuarios[username] = password
        
        with open(archivo, "w", encoding = "utf-8") as u:
            json.dump(usuarios, u, indent = 4)
        
        print("Usuario guardado")
    
    return usuarios


# Login
def login_usuario(usuarios):
    print("\n---- Login ----")
    
    intentos_restantes = 3
    
    while intentos_restantes > 0:
        user_login = input("Usuario: ").strip()
        pass_login = input("Contraseña: ").strip()
        
        if user_login in usuarios and usuarios[user_login] == pass_login:
            print("Login correcto")
            return user_login
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos_restantes}")
            else:
                print("Máximo de intentos alcanzado. Acceso denegado.")
    
    return False





