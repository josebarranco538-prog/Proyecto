


from Producto import Producto
from MG_Producto import definir_archivo, cargar_productos, guardar_productos
from MG_Usuarios import definir_archivo as definir_archivo_usuarios, cargar_usuarios
from MG_Carrito import definir_archivo as definir_archivo_compras, mostrar_compras
import json
from pathlib import Path


class Admin:
    # Constructor que define los archivos de productos, usuarios y compras
    def __init__(self):
        self.__archivo_productos = definir_archivo()
        self.__archivo_usuarios = definir_archivo_usuarios()
        self.__archivo_compras = definir_archivo_compras()
    
    # Metodo para ver los productos
        productos = cargar_productos(self.__archivo_productos)
        if not productos:
            print("No hay productos disponibles.")
        else:
            print("\n---- Productos ----")
            for i, p in enumerate(productos, 1):
                print(f"{i}. {p.nombre()} - ${p.precio()} - Stock: {p.stock()}")
    
    # Metodo para agregar los productos verificando que no exista un producto con el mismo nombre
    # Para evitar duplicados, y guardando los cambios en el archivo json
    def agregar_producto(self, nombre, precio, stock):
        productos = cargar_productos(self.__archivo_productos)
        # Verificar si el producto ya existe
        for p in productos:
            if p.nombre().lower() == nombre.lower():
                print("El producto ya existe.")
                return
        nuevo_producto = Producto(nombre, precio, stock)
        productos.append(nuevo_producto)
        guardar_productos(self.__archivo_productos, productos)
        print(f"Producto '{nombre}' agregado exitosamente.")
    
    # Metodo para eliminar los productos por el nombre
    def eliminar_producto(self, nombre):
        productos = cargar_productos(self.__archivo_productos)
        producto_encontrado = False
        for i, p in enumerate(productos):
            if p.nombre().lower() == nombre.lower():
                productos.pop(i)
                producto_encontrado = True
                guardar_productos(self.__archivo_productos, productos)
                print(f"Producto '{nombre}' eliminado exitosamente.")
                break
        if not producto_encontrado:
            print(f"Producto '{nombre}' no encontrado.")
    
    # Metodo para modificar el precio de un producto por su nombre
    def modificar_precio(self, nombre, nuevo_precio):
        productos = cargar_productos(self.__archivo_productos)
        producto_encontrado = False
        for p in productos:
            if p.nombre().lower() == nombre.lower():
                p.set_precio(nuevo_precio)
                producto_encontrado = True
                guardar_productos(self.__archivo_productos, productos)
                print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
                break
        if not producto_encontrado:
            print(f"Producto '{nombre}' no encontrado.")
    
    # Metodo para modificar el stock de un producto por su nombre
    def modificar_stock(self, nombre, nuevo_stock):
        productos = cargar_productos(self.__archivo_productos)
        producto_encontrado = False
        for p in productos:
            if p.nombre().lower() == nombre.lower():
                p.set_stock(nuevo_stock)
                producto_encontrado = True
                guardar_productos(self.__archivo_productos, productos)
                print(f"Stock de '{nombre}' actualizado a {nuevo_stock} unidades.")
                break
        if not producto_encontrado:
            print(f"Producto '{nombre}' no encontrado.")
    
    # Metodo para ver los usuarios registrados mostrando su nombre y contrasena (solo para admin)
    def ver_usuarios(self):
        usuarios = cargar_usuarios(self.__archivo_usuarios)
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("\n---- Usuarios ----")
            for i, (usuario, contrasena) in enumerate(usuarios.items(), 1):
                print(f"{i}. {usuario} - Contrasena: {contrasena}")
    
    # Metodo para eliminar un usuario por su nombre
    def eliminar_usuario(self, usuario):
        usuarios = cargar_usuarios(self.__archivo_usuarios)
        
        if usuario in usuarios:
            del usuarios[usuario]
            with open(self.__archivo_usuarios, "w", encoding = "utf-8") as u:
                json.dump(usuarios, u, indent = 4)
            print(f"Usuario '{usuario}' eliminado exitosamente.")
        else:
            print(f"Usuario '{usuario}' no encontrado.")
    
    # Metodo para ver el historial de compras mostrando el usuario, productos comprados, total y fecha de compra
    def ver_historial_compras(self):
        mostrar_compras(self.__archivo_compras)
    
    # Metodo para generar un reporte de ventas mostrando el total de ventas, cantidad de compras y productos mas vendidos
    def generar_reporte_ventas(self):
        with open(self.__archivo_compras, "r", encoding = "utf-8") as c:
            compras = json.load(c)
        if not compras:
            print("No hay compras registradas.")
            return
        total_ventas = 0
        cantidad_compras = len(compras)
        productos_vendidos = {}
        for compra in compras:
            total_ventas += compra["total"]
            for producto in compra["productos"]:
                nombre = producto["nombre"]
                cantidad = producto["cantidad"]
                if nombre in productos_vendidos:
                    productos_vendidos[nombre] += cantidad
                else:
                    productos_vendidos[nombre] = cantidad
        print("\n---- Reporte de Ventas ----")
        print(f"Total de compras: {cantidad_compras}")
        print(f"Total de ventas: ${total_ventas}")
        print("\nProductos mas vendidos:")
        for producto, cantidad in sorted(productos_vendidos.items(), key = lambda x: x[1], reverse = True):
            print(f"  - {producto}: {cantidad} unidades")

    # Menu para el admin con opciones para gestionar productos, usuarios, historial de compras y reporte de ventas
    def menu_admin(self):
        while True:
            print("\n---- Panel de Administracion ----")
            print("1. Ver productos")
            print("2. Agregar producto")
            print("3. Eliminar producto")
            print("4. Modificar precio")
            print("5. Modificar stock")
            print("6. Ver usuarios")
            print("7. Eliminar usuario")
            print("8. Ver historial de compras")
            print("9. Generar reporte de ventas")
            print("10. Salir")
            
            try:
                opcion = int(input("Seleccione una opcion: "))
                
                match opcion:
                    case 1:
                        self.ver_productos()
                    
                    case 2:
                        nombre = input("Nombre del producto: ").strip()
                        try:
                            precio = int(input("Precio: "))
                            stock = int(input("Stock: "))
                            self.agregar_producto(nombre, precio, stock)
                        except ValueError:
                            print("Precio y stock deben ser numeros.")
                    
                    case 3:
                        nombre = input("Nombre del producto a eliminar: ").strip()
                        self.eliminar_producto(nombre)
                    
                    case 4:
                        nombre = input("Nombre del producto: ").strip()
                        try:
                            nuevo_precio = int(input("Nuevo precio: "))
                            self.modificar_precio(nombre, nuevo_precio)
                        except ValueError:
                            print("El precio debe ser un numero.")
                    
                    case 5:
                        nombre = input("Nombre del producto: ").strip()
                        try:
                            nuevo_stock = int(input("Nuevo stock: "))
                            self.modificar_stock(nombre, nuevo_stock)
                        except ValueError:
                            print("El stock debe ser un numero.")
                    
                    case 6:
                        self.ver_usuarios()
                    
                    case 7:
                        usuario = input("Usuario a eliminar: ").strip()
                        self.eliminar_usuario(usuario)
                    
                    case 8:
                        self.ver_historial_compras()
                    
                    case 9:
                        self.generar_reporte_ventas()
                    
                    case 10:
                        print("Saliendo del panel de administracion...")
                        break
                    
                    case _:
                        print("Opcion no valida. Ingrese un numero entre 1 y 10.")
            
            except ValueError:
                print("Entrada invalida. Ingrese un numero.")

















