


class Producto:
    # Constructor para inicializar un producto con su nombre, precio, stock y descuento
    def __init__(self, nombre, precio, stock = 0, descuento = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = 1
        self.__stock = stock
        self.__descuento = descuento
    
    # Metodos para acceder y modificar los atributos del producto
    def nombre(self):
        return self.__nombre
    
    def precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock
    
    # Metodo para descontar stock al realizar una venta
    def descontar_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False
    
    # Metodo para acceder, modificar, calcular el precio con descuento y mostrar el descuento del producto
    def descuento(self):
        return self.__descuento
    
    def set_descuento(self, descuento):
        self.__descuento = descuento
    
    def precio_con_descuento(self):
        return self.__precio * (1 - self.__descuento)
    
    def mostrar_producto(self):
        print(f" {self.__nombre} - Precio: ${self.__precio} - Stock: {self.__stock} - Descuento: {self.__descuento * 100:.0f}%")










