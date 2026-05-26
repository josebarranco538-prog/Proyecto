


import json
from pathlib import Path


# Define el archivo de usuarios en descargas
def definir_archivo():
    archivo = Path.home() / "Downloads" / "usuarios.json"
    print("Archivo se guardara en:", archivo)
    return archivo


# Crea el archivo si no existe
def crear_archivo_si_no_existe(archivo):
    if not archivo.exists():
        print("Archivo no existe, creando uno nuevo...")
        with open(archivo, "w", encoding = "utf-8") as u:
            json.dump({}, u)
    else:
        print("Archivo ya existe")


# Carga los usuarios desde el archivo json y retorna un diccionario con los datos
def cargar_usuarios(archivo):
    with open(archivo, "r", encoding = "utf-8") as u:
        usuarios = json.load(u)
    return usuarios


# Menu de gestion de usuarios para login, registro e inicio de sesion como admin
# Retorna el nombre del usuario logueado o False si no se pudo loguear
def menu_gestion_usuarios(archivo_usuarios, usuarios):
    while True:
        print("\n---- Gestion de Usuarios ----")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Iniciar sesion como Admin")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opcion: "))
            
            match opcion:
                case 1:
                    # Iniciar sesion
                    print("\n---- Login ----")
                    
                    intentos_restantes = 3
                    
                    while intentos_restantes > 0:
                        user_login = input("Usuario: ").strip()
                        pass_login = input("Contrasena: ").strip()
                        
                        if user_login in usuarios and usuarios[user_login] == pass_login:
                            print("Login correcto")
                            return user_login
                        else:
                            intentos_restantes -= 1
                            if intentos_restantes > 0:
                                print(f"Usuario o contrasena incorrectos. Intentos restantes: {intentos_restantes}")
                            else:
                                print("Maximo de intentos alcanzado. Acceso denegado.")
                    return False
                
                case 2:
                    # Registrarse
                    print("\n---- Registro ----")
                    
                    username = input("Usuario: ").strip()
                    password = input("Contrasena: ").strip()
                    
                    if username in usuarios:
                        print("Ese usuario ya existe")
                    else:
                        usuarios[username] = password
                    
                    with open(archivo_usuarios, "w", encoding = "utf-8") as u:
                        json.dump(usuarios, u, indent = 4)
                    
                    print("Usuario guardado")
                
                case 3:
                    # Iniciar sesion como Admin
                    print("\n---- Login Admin ----")
                    
                    intentos_restantes = 3
                    contrasena_admin = "admin123"
                    
                    while intentos_restantes > 0:
                        pass_admin = input("Contrasena de Admin: ").strip()
                        
                        if pass_admin == contrasena_admin:
                            print("Login de Admin correcto")
                            from Admin import Admin
                            admin = Admin()
                            admin.menu_admin()
                            break
                        else:
                            intentos_restantes -= 1
                            if intentos_restantes > 0:
                                print(f"Contrasena incorrecta. Intentos restantes: {intentos_restantes}")
                            else:
                                print("Maximo de intentos alcanzado. Acceso denegado.")
                
                case 4:
                    # Salir
                    print("Saliendo")
                    exit()
                
                case _:
                    print("Opcion no valida. Ingrese un numero entre 1 y 4.")
        
        except ValueError:
            print("Entrada invalida. Ingrese un numero entre 1 y 4.")







