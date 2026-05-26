


class Carrito:
    # Constructor del carrito de compras que inicializa una lista vacia de productos
    def __init__(self):
        self.__productos = []
    
    # Metodo para obtener la lista de productos en el carrito
    def productos(self):
        return self.__productos
    
    # Metodo para agregar un producto al carrito. Si el producto ya existe, se actualiza la cantidad
    def agregar_producto(self, producto, cantidad = 1):
        for item in self.__productos:
            if item.nombre() == producto.nombre():
                item.set_cantidad(item.cantidad() + cantidad)
                print(f"Cantidad actualizada. {item.nombre()} x{item.cantidad()}")
                return
        producto.set_cantidad(cantidad)
        self.__productos.append(producto)
        print(f"{producto.nombre()} x{cantidad} agregado al carrito.")
    
    # Metodo para mostrar los productos en el carrito con sus precios, descuentos y subtotales
    def mostrar_carrito(self):
        if not self.__productos:
            print("Carrito vacio.")
        else:
            for i, item in enumerate(self.__productos, 1):
                precio_unitario = item.precio()
                descuento = item.descuento()
                if descuento > 0:
                    precio_con_descuento = item.precio_con_descuento()
                    subtotal = precio_con_descuento * item.cantidad()
                    print(f"{i}. {item.nombre()} x{item.cantidad()} - ${precio_unitario} (Descuento: {int(descuento*100)}%) -> ${precio_con_descuento} - Subtotal: ${subtotal}")
                else:
                    subtotal = precio_unitario * item.cantidad()
                    print(f"{i}. {item.nombre()} x{item.cantidad()} - ${precio_unitario} - Subtotal: ${subtotal}")
    
    # Metodo para calcular el total del carrito, aplicando descuentos si corresponden
    def calcular_total(self):
        total = 0
        for item in self.__productos:
            if item.descuento() > 0:
                total += item.precio_con_descuento() * item.cantidad()
            else:
                total += item.precio() * item.cantidad()
        return total
    
    # Metodo para vaciar el carrito, eliminando todos los productos
    def vaciar_carrito(self):
        self.__productos.clear()
    
    # Metodo para eliminar un producto del carrito por su indice o reducir su cantidad
    def eliminar_producto(self, indice, cantidad = None):
        if 0 <= indice < len(self.__productos):
            producto = self.__productos[indice]
            if cantidad is None or cantidad >= producto.cantidad():
                # Eliminar todo el producto
                eliminado = self.__productos.pop(indice)
                print(f"{eliminado.nombre()} eliminado del carrito.")
            else:
                # Reducir la cantidad
                producto.set_cantidad(producto.cantidad() - cantidad)
                print(f"Se removieron {cantidad} unidades de {producto.nombre()}. Quedan {producto.cantidad()} unidades.")
        else:
            print("Indice no valido.")







