


from Sistema import Sistema
from Producto import Producto
from Carrito import Carrito
from Usuario import Usuario
from MG_Producto import definir_archivo, cargar_productos, guardar_productos
from MG_Usuarios import definir_archivo as definir_archivo_usuarios, crear_archivo_si_no_existe, cargar_usuarios, registrar_usuario, login_usuario


def menu_gestion_usuarios(archivo_usuarios, usuarios):
    
    while True:
        print("\n---- Gestión de Usuarios ----")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            match opcion:
                case 1:
                    # Iniciar sesión
                    usuario_nombre = login_usuario(usuarios)
                    if usuario_nombre:
                        Usuario.usuario_actual = Usuario(usuario_nombre, usuarios[usuario_nombre])
                        return usuario_nombre
                    else:
                        print("Intente nuevamente.")
                
                case 2:
                    # Registrarse
                    usuarios = registrar_usuario(archivo_usuarios, usuarios)
                    print("Registro completado. Ahora inicie sesión.")
                
                case 3:
                    # Salir
                    print("Saliendo...")
                    exit()
                
                case _:
                    print("Opción no válida. Ingrese un número entre 1 y 3.")
        
        except ValueError:
            print("Entrada inválida. Ingrese un número entre 1 y 3.")


# Gestión de Usuarios
archivo_usuarios = definir_archivo_usuarios()
crear_archivo_si_no_existe(archivo_usuarios)
usuarios = cargar_usuarios(archivo_usuarios)

# Mostrar menú de gestión de usuarios
usuario_nombre = menu_gestion_usuarios(archivo_usuarios, usuarios)

# Cargar Productos desde json
archivo = definir_archivo()
productos_cargados = cargar_productos(archivo)

sistema = Sistema()

# Agregar productos cargados
for producto in productos_cargados:
    sistema.productos().append(producto)

# Si no hay productos, agregar los productos
if not productos_cargados:
    sistema.productos().append(Producto("Hamburguesa clásica", 36000, 200))
    sistema.productos().append(Producto("Papas fritas", 18000, 200))
    sistema.productos().append(Producto("Refresco cola", 10000, 200))
    sistema.productos().append(Producto("Hot dog", 29000, 200))
    
    # Guardar productos en json
    guardar_productos(archivo, sistema.productos())

sistema.run()


