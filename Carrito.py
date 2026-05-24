


class Carrito:
    def __init__(self):
        self.__productos = []

    def productos(self):
        return self.__productos

    def agregar_producto(self, producto, cantidad=1):
        for item in self.__productos:
            if item.nombre() == producto.nombre():
                item.set_cantidad(item.cantidad() + cantidad)
                print(f"Cantidad actualizada. {item.nombre()} x{item.cantidad()}")
                return
        producto.set_cantidad(cantidad)
        self.__productos.append(producto)
        print(f"{producto.nombre()} x{cantidad} agregado al carrito.")

    def mostrar_carrito(self):
        if not self.__productos:
            print("Carrito vacío.")
        else:
            for i, item in enumerate(self.__productos, 1):
                print(f"{i}. {item.nombre()} x{item.cantidad()} - ${item.precio()} - Subtotal: ${item.precio() * item.cantidad()}")

    def calcular_total(self):
        return sum(item.precio() * item.cantidad() for item in self.__productos)

    def vaciar_carrito(self):
        self.__productos.clear()

    def eliminar_producto(self, indice):
        if 0 <= indice < len(self.__productos):
            eliminado = self.__productos.pop(indice)
            print(f"{eliminado.nombre()} eliminado del carrito.")
        else:
            print("Índice no válido.")







