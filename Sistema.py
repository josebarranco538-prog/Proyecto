


from Carrito import Carrito
from Usuario import Usuario
from Producto import Producto
from MG_Carrito import definir_archivo, guardar_compra
from MG_Tarjetas import definir_archivo as definir_archivo_tarjetas, crear_archivo_si_no_existe, cargar_datos_tarjeta, guardar_datos_tarjeta, verificar_saldo, descontar_saldo

class Sistema:
    # Se inicializa el sistema con productos, carrito, archivos y menu
    def __init__(self):
        self.__productos = []
        self.__carrito = Carrito()
        self.__archivo_compras = definir_archivo()
        self.__archivo_tarjetas = definir_archivo_tarjetas()
        crear_archivo_si_no_existe(self.__archivo_tarjetas)
        self.__menu = "\n---- Munchy's Hub ----\n1. Ver productos disponibles.\n2. Agregar producto al carrito.\n3. Ver carrito.\n4. Pagar.\n5. Salir."
        self.__estado = True
    
    # Getter para productos
    def productos(self):
        return self.__productos
    
    # Metodo principal para ejecutar el sistema
    def run(self):
        # Gestion del menu principal con opciones para ver productos, agregar al carrito, ver carrito, pagar y salir
        while self.__estado:
            try:
                opcion = int(input(self.__menu+"\nSeleccione la opcion deseada: "))
                if opcion < 1 or opcion > 5:
                    raise ValueError
            except ValueError:
                print("Entrada invalida, seleccione un numero entre (1 - 5)")
                continue
                
                # Manejo de cada opcion del menu usando match-case
            match opcion:
                # Muestra los productos disponibles
                case 1:
                    print("\n---- Productos disponibles ----")
                    for i, p in enumerate(self.__productos, 1):
                        print(f"{i}. ", end="")
                        p.mostrar_producto()
                
                # Agrega productos al carrito
                case 2:
                    while True:
                        print("\n---- Productos ----")
                        for i, p in enumerate(self.__productos, 1):
                            print(f"{i}. ", end="")
                            p.mostrar_producto()
                        print("0. Salir")
                        try:
                            selec = int(input("Seleccione el producto a agregar (numero): "))
                            if selec == 0:
                                break
                            if 1 <= selec <= len(self.__productos):
                                cantidad = int(input("Cuantos desea llevar?: "))
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
                
                # Muestra los productos en el carrito
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
                                cantidad_eliminar = int(input("Cuantas unidades desea eliminar?: "))
                                self.__carrito.eliminar_producto(indice, cantidad_eliminar)
                            except ValueError:
                                print("Entrada invalida.")
                
                # Procesa el pago, guarda la compra y descuenta los productos del stock
                case 4:
                    if Usuario.usuario_actual:
                        print(f"\nPedido de {Usuario.usuario_actual.nombre()}:")
                    self.__carrito.mostrar_carrito()
                    total = self.__carrito.calcular_total()
                    # Aplica los descuento por nivel de compra
                    descuento_aplicado = 0
                    if total > 600000:
                        descuento_aplicado = total * 0.15
                        print(f"\nDescuento por compra mayor a 600k -${descuento_aplicado:.0f} (15%)")
                    elif total > 300000:
                        descuento_aplicado = total * 0.10
                        print(f"\nDescuento por compra mayor a 300k -${descuento_aplicado:.0f} (10%)")
                    elif total > 150000:
                        descuento_aplicado = total * 0.05
                        print(f"\nDescuento por compra mayor a 150k -${descuento_aplicado:.0f} (5%)")
                    else:
                        print("\nNo aplica descuento para compras menores a $150.000")
                    total -= descuento_aplicado
                    print(f"Total a pagar: ${total:.0f}")
                    # Guarda la compra y descuenta del stock
                    if self.__carrito.productos:
                        # Carga datos de tarjeta guardados o pide nuevos
                        nombre_usuario = Usuario.usuario_actual.nombre() if Usuario.usuario_actual else "invitado"
                        datos_tarjeta = cargar_datos_tarjeta(self.__archivo_tarjetas, nombre_usuario)
                        if datos_tarjeta:
                            print(f"\nUsando tarjeta guardada: {datos_tarjeta["numero_tarjeta"][-4:]}")
                            usar_guardada = input("Desea usar esta tarjeta? (s/n): ").strip().lower()
                            if usar_guardada != 's':
                                numero_tarjeta = input("Ingrese el numero de tarjeta: ").strip()
                                cvc = input("Ingrese el CVC: ").strip()
                                if not guardar_datos_tarjeta(self.__archivo_tarjetas, nombre_usuario, numero_tarjeta, cvc):
                                    continue
                        else:
                            numero_tarjeta = input("Ingrese el numero de tarjeta: ").strip()
                            cvc = input("Ingrese el CVC: ").strip()
                            if not guardar_datos_tarjeta(self.__archivo_tarjetas, nombre_usuario, numero_tarjeta, cvc):
                                continue
                        # Verifica el saldo antes de procesar la compra
                        if verificar_saldo(self.__archivo_tarjetas, nombre_usuario, total):
                            guardar_compra(self.__archivo_compras, self.__carrito, Usuario.usuario_actual)
                            # Descuenta la cantidad de productos del stock
                            for item in self.__carrito.productos():
                                item.descontar_stock(item.cantidad())
                            # Guarda los productos con nuevo stock
                            from MG_Producto import guardar_productos, definir_archivo as definir_archivo_productos
                            archivo_productos = definir_archivo_productos()
                            guardar_productos(archivo_productos, self.__productos)
                            # Descuenta el saldo de la tarjeta
                            descontar_saldo(self.__archivo_tarjetas, nombre_usuario, total)
                            print("Compra guardada.")
                            self.__carrito.vaciar_carrito()
                            print("Pago realizado. Carrito vaciado.")
                        else:
                            print("Saldo insuficiente en la tarjeta.")
                
                case 5:
                    self.__estado = False
                    print("Saliendo")
















