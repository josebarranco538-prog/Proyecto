


from Carrito import Carrito
from Usuario import Usuario
from MG_Carrito import definir_archivo, guardar_compra

class Sistema:

    def __init__(self):
        self.__productos = []
        self.__carrito = Carrito()
        self.__archivo_compras = definir_archivo()
        self.__menu = "\n---- Munchy's Hub ----\n1. Ver productos disponibles.\n2. Agregar producto al carrito.\n3. Ver carrito.\n4. Pagar.\n5. Salir."
        self.__estado = True

    def productos(self):
        return self.__productos

    def carrito(self):
        return self.__carrito

    def run(self):
        while self.__estado:
            try:
                opcion = int(input(self.__menu+"\nSeleccione la opcion deseada: "))
                if opcion < 1 or opcion > 5:
                    raise ValueError
            except ValueError:
                print("Entrada invalida, seleccione un numero entre (1 - 5)")
                continue

            match opcion:
                case 1:
                    print("\n---- Productos disponibles ----")
                    self.mostrar_productos()

                case 2:
                    while True:
                        print("\n---- Productos ----")
                        self.mostrar_productos()
                        print("0. Salir al menú principal")
                        try:
                            selec = int(input("Seleccione el producto a agregar (numero): "))
                            if selec == 0:
                                break
                            if 1 <= selec <= len(self.__productos):
                                cantidad = int(input("¿Cuántos desea llevar? "))
                                producto_seleccionado = self.__productos[selec - 1]
                                if cantidad > 0:
                                    if cantidad <= producto_seleccionado.stock():
                                        self.__carrito.agregar_producto(producto_seleccionado, cantidad)
                                    else:
                                        print(f"Stock insuficiente. Disponibles: {producto_seleccionado.stock()}")
                                else:
                                    print("La cantidad debe ser mayor a 0.")
                            else:
                                print("Producto no valido.")
                        except ValueError:
                            print("Entrada invalida.")

                case 3:
                    if Usuario.usuario_actual:
                        print(f"\nCarrito de {Usuario.usuario_actual.nombre()}:")
                    self.__carrito.mostrar_carrito()
                    if self.__carrito.productos:
                        total_carrito = self.__carrito.calcular_total()
                        print(f"Total del carrito: ${total_carrito}")
                        eliminar = input("Desea eliminar un producto del carrito? (s/n): ").strip().lower()
                        if eliminar == 's':
                            try:
                                indice = int(input("Ingrese el numero del producto a eliminar: ")) - 1
                                self.__carrito.eliminar_producto(indice)
                            except ValueError:
                                print("Entrada invalida.")

                case 4:
                    if Usuario.usuario_actual:
                        print(f"\nPedido de {Usuario.usuario_actual.nombre()}:")
                    self.__carrito.mostrar_carrito()
                    total = self.__carrito.calcular_total()
                    print(f"Total a pagar: ${total}")
                    
                    # Guardar la compra y descontar del stock
                    if self.__carrito.productos:
                        guardar_compra(self.__archivo_compras, self.__carrito, Usuario.usuario_actual)
                        # Descontar cantidad del stock
                        for item in self.__carrito.productos():
                            item.descontar_stock(item.cantidad())
                        # Guardar productos con nuevo stock
                        from MG_Producto import guardar_productos, definir_archivo as definir_archivo_productos
                        archivo_productos = definir_archivo_productos()
                        guardar_productos(archivo_productos, self.__productos)
                        print("Compra guardada.")
                    
                    self.__carrito.vaciar_carrito()
                    print("Pago realizado. Carrito vaciado.")

                case 5:
                    self.__estado = False
                    print("Saliendo...")

    def mostrar_productos(self):
        if not self.__productos:
            print("No hay productos disponibles.")
        else:
            for i, p in enumerate(self.__productos, 1):
                print(f"{i}. {p.nombre()} - ${p.precio()} - Stock: {p.stock()}")
















