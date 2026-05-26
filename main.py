


from Sistema import Sistema
from Producto import Producto
from Carrito import Carrito
from Usuario import Usuario
from MG_Usuarios import definir_archivo as definir_archivo_usuarios, crear_archivo_si_no_existe, cargar_usuarios, menu_gestion_usuarios
from MG_Producto import definir_archivo as definir_archivo_productos, cargar_productos, guardar_productos, crear_archivo_si_no_existe as crear_archivo_productos
from MG_Promociones import definir_archivo as definir_archivo_promociones, obtener_descuentos_del_dia


# Gestion de Usuarios
archivo_usuarios = definir_archivo_usuarios()
crear_archivo_si_no_existe(archivo_usuarios)
usuarios = cargar_usuarios(archivo_usuarios)


# Mostrar menu de gestion de usuarios
usuario_nombre = menu_gestion_usuarios(archivo_usuarios, usuarios)


# Crear sistema
sistema = Sistema()


# Cargar productos del archivo o crear iniciales si no existen
archivo_productos = definir_archivo_productos()
crear_archivo_productos(archivo_productos)
productos_cargados = cargar_productos(archivo_productos)

if not productos_cargados:
    # Si el archivo esta vacio, crear productos iniciales
    productos_iniciales = [
        Producto("Hamburguesa clasica", 36000, 200),
        Producto("Papas fritas", 18000, 200),
        Producto("Refresco cola", 10000, 200),
        Producto("Hot dog", 29000, 200),
        Producto("Pizza pequena", 45000, 150),
        Producto("Pizza grande", 75000, 120),
        Producto("Alitas de pollo", 28000, 200),
        Producto("Nuggets de pollo", 22000, 250),
        Producto("Cheeseburger", 40000, 160),
        Producto("Pollo frito", 33000, 200),
        Producto("Papas crujientes", 16000, 120),
        Producto("Papas con queso", 14000, 180),
        Producto("Soda naranja", 8000, 300),
        Producto("Hamburguesa especial", 50000, 140),
        Producto("Empanadas", 12000, 300),
        Producto("Sandwich de atun", 26000, 160),
        Producto("Alitas BBQ", 40000, 170),
        Producto("Coca Cola", 11000, 250),
        Producto("Sprite", 11000, 250),
        Producto("Fanta uva", 10000, 280)
    ]
    sistema.productos().extend(productos_iniciales)
    guardar_productos(archivo_productos, sistema.productos())
else:
    # Usar los productos cargados del archivo
    sistema.productos().extend(productos_cargados)

# Aplicar descuentos rotativos del dia
archivo_promociones = definir_archivo_promociones()
nombres_descuento = obtener_descuentos_del_dia(archivo_promociones, sistema.productos())

for nombre_producto in nombres_descuento:
    for producto in sistema.productos():
        if producto.nombre() == nombre_producto:
            producto.set_descuento(0.20)
            break

# Guardar productos con los descuentos aplicados
guardar_productos(archivo_productos, sistema.productos())


# Ejecutar el sistema
sistema.run()


