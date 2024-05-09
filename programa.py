# 3. En un archivo programa.py, implementa la lógica necesaria para crear una tienda e
# ingresar sus productos. Se debe solicitar ingresar productos hasta que el usuario
# indique lo contrario. Luego, se le debe dar al usuario las opciones de listar los
# productos existentes, realizar una venta, o salir del programa. Para las primeras dos
# opciones, debe hacer llamados a los métodos de su instancia y luego volver a
# consultar cuál de las tres acciones se desea realizar. Si se escoge la tercera opción,
# se finaliza la ejecución del programa.


# Existen por el momento 3 tipos de tienda (en el futuro podría haber más), los cuales
# son: “Restaurante”, “Supermercado” y “Farmacia”.
# ● Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y
# realizar ventas.
# ● Cada tienda creada, independiente de su tipo, posee un nombre, un listado de
# productos y un costo de delivery. Al momento de crear una nueva tienda, se debe
# solicitar el nombre y el costo de delivery (todas las tiendas se crean inicialmente sin
# productos). En una tienda ya existente, no se puede modificar el nombre ni el costo de
# delivery, pero sí se puede modificar los productos (mediante el ingreso de un producto,
# o mediante la realización de ventas).
# ● Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben solicitar
# al momento de crear un producto nuevo, pero si no se indica stock, se asume que es
# 0. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se
# intenta modificar el stock por un valor menor a 0, se debe asignar 0 en su lugar. De
# cada producto se puede obtener su nombre, su precio o su stock.

# NOTA: Se asume que cada producto es específico de una tienda. Es decir, un
# producto no existe por sí mismo, sino que como parte de una tienda.
# Respecto del comportamiento de cada tipo de tienda, considere lo siguiente:
# ● Para ingresar un producto a una tienda, se debe solicitar los datos requeridos del
# producto. Una vez creado el producto, éste se añade a la lista de productos a la tienda.
# Si el producto ya existe en la tienda (dado por su nombre), se debe modificar su stock,
# sumando al valor existente el stock del nuevo ingreso. Se conserva el precio del primer
# ingreso de un mismo producto. Tip: Pruebe sobrecargar los operadores __add__,
# __sub__ y __eq__.
# NOTA: Los productos de las tiendas de tipo “Restaurante” siempre tienen stock igual
# a 0, ya que el producto solo se fabrica al momento de que se realiza una venta. Es
# decir, aunque se especifique un valor de stock, los productos de estas tiendas se
# crean con stock 0 y este no se modifica si se añade nuevamente el
#  mismo producto a la lista de productos existentes de la tienda.
# ● Al listar los productos existentes, se debe ocultar el stock de los productos en el caso
# de las tiendas de tipo Restaurante y Farmacia. Las tiendas de tipo Supermercado
# deben añadir el mensaje “Pocos productos disponibles” junto a la cantidad de stock
# del producto, en caso de que el stock del producto sea inferior a 10. Las tiendas de
# tipo Farmacia deben añadir el mensaje “Envío gratis al solicitar este producto” junto al
# precio de los productos con un valor superior a $15.000.
# NOTA: Considera que el método para listar los productos será llamado dentro de
# print, por lo que debe retornar un string.
# ● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender
# y la cantidad requerida. Las tiendas de tipo Farmacia y Supermercado deben tener
# stock existente del producto indicado (si no poseen stock, o no existe el producto
# solicitado, no se realiza ninguna acción). Sin embargo, los productos de las tiendas de
# tipo Restaurante siempre tienen stock 0, por lo que no es necesario hacer esta
# validación ni modificar el stock (Tip: puede usar pass). Además, en el caso específico
# de las tiendas de tipo Farmacia, no se puede solicitar una cantidad superior a 3 por
# producto en cada venta (si se solicita una cantidad mayor a 3, no se realiza ninguna
# acción). En el caso de las tiendas de tipo Farmacia o Supermercado, si la cantidad
# _ 3
# www.desafiolatam.com
# requerida es superior a la existente, solo se venderá la cantidad disponible (quedando
# entonces el stock del producto en 0).


from tienda import Restaurante, Farmacia, Supermercado
from producto import Product


def create_store():
    while True:
        print("Seleccione un tipo de tienda con su numero correspondiente:")
        print("1. Restaurante")
        print("2. Supermercado")
        print("3. Farmacia")

        tienda_type = input("Seleccione una opción: \n>>>")

        if tienda_type == "1":
            tienda_name = input("Seleccione un Nombre: \n>>>")
            tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
            tienda = Restaurante(tienda_name, tienda_delivery)
            return tienda
        elif tienda_type == "2":
            tienda_name = input("Seleccione un Nombre: \n>>>")
            tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
            tienda = Supermercado(tienda_name, tienda_delivery)
            return tienda
        elif tienda_type == "3":
            tienda_name = input("Seleccione un Nombre: \n>>>")
            tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
            tienda = Farmacia(tienda_name, tienda_delivery)
            return tienda
        else:
            print('opcion invalida\n')

def main():
    # Crear una instancia de Tienda
    tienda = create_store()

    #ingreso productos
    ingresar_productos(tienda)


    while True:
        print("\nAcciones disponibles:")
        print("1. Listar productos existentes")
        print("2. Realizar una venta")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_productos(tienda)
        elif opcion == "2":
            realizar_venta(tienda)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ingresar_productos(tienda):
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        tienda.ingress_products(nombre, precio, stock)

        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break

def listar_productos(tienda):
    print("\nProductos existentes:")
    print(tienda.list_products())


def realizar_venta(tienda):
    nombre_producto = input("Ingrese el nombre del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))

    tienda.sales(nombre_producto, cantidad)



# first_question = True

# while True:
#     while first_question:
#         print("Seleccione un tipo de tienda con su numero correspondiente:")
#         print("1. Restaurante")
#         print("2. Supermercado")
#         print("3. Farmacia")

#         tienda_type = input("Seleccione una opción: \n>>>")

#         if tienda_type == "1":
#             tienda_name = input("Seleccione un Nombre: \n>>>")
#             tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
#             tienda = Restaurante(tienda_name, tienda_delivery)
#             break
#         elif tienda_type == "2":
#             tienda_name = input("Seleccione un Nombre: \n>>>")
#             tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
#             tienda = Supermercado(tienda_name, tienda_delivery)
#             break
#         elif tienda_type == "3":
#             tienda_name = input("Seleccione un Nombre: \n>>>")
#             tienda_delivery = input("Seleccione el costo del delivery: \n>>>")
#             tienda = Farmacia(tienda_name, tienda_delivery)
#             break
#         else:
#             print('opcion invalida\n')
#     first_question = False
    
#     print("Menú:")
#     print("1. Ingresar productos")
#     print("2. Listar productos")
#     print("3. Realizar venta")
#     print("4. Salir")

#     opcion = input("Seleccione una opción: \n>>>")

#     if opcion == "1":
#         nombre_producto = input("Ingrese el nombre del producto: ")
#         precio_producto = float(input("Ingrese el precio del producto: "))
#         stock_producto = int(input("Ingrese el stock del producto: "))
#         tienda.ingress_products(nombre_producto, precio_producto, stock_producto)
#         print("Producto ingresado correctamente.")
#     elif opcion == "2":
#         print("Productos existentes:")
#         print(tienda.list_products())
#     elif opcion == "3":
#         nombre_producto = input("Ingrese el nombre del producto a vender: ")
#         cantidad = int(input("Ingrese la cantidad a vender: "))
#         tienda.sales(nombre_producto, cantidad)
#     elif opcion == "4":
#         exit()
#     else:
#         print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()