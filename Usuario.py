


class Usuario:
    usuario_actual = False
    
    # Constructor de la clase Usuario que recibe el nombre y la contrasena del usuario.
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
    
    # Metodo para obtener el nombre del usuario
    def nombre(self):
        return self.__nombre
    
    # Metodo para obtener la contrasena del usuario
    def contrasena(self):
        return self.__contrasena





