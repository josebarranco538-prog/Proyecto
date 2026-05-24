


class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = 1
        self.__stock = stock

    def nombre(self):
        return self.__nombre

    def precio(self):
        return self.__precio

    def cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = stock

    def descontar_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

    def mostrar_producto(self):
        print(f"\n{self.__nombre}\n- ${self.__precio}\n- Cantidad: {self.__cantidad}\n- Stock disponible: {self.__stock}")




