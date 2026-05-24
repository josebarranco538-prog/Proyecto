


class Usuario:
    clientes = []
    usuario_actual = False

    def __init__(self, nombre, contraseña):
        self.__nombre = nombre
        self.__contraseña = contraseña
        Usuario.clientes.append(self)

    def nombre(self):
        return self.__nombre
    
    def contraseña(self):
        return self.__contraseña

    def mostrar_usuario(self):
        print(f"{self.__nombre}")





