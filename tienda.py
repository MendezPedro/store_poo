# En un archivo tienda.py, definir la o las clases necesarias para instanciar los distintos
# tipos de tienda (utilice ABSTRACCIÓN y ENCAPSULAMIENTO). Cada clase que
# permita instanciar una tienda debe tener (considerar para cada punto la información
# entregada en la descripción de la problemática):
# a. Un método constructor (1 Punto)
# b. Un método para ingresar un producto (utilice COMPOSICIÓN, y opcionalmente
# COLABORACIÓN) (2 Puntos)
# c. Un método para listar productos (1 Punto)
# d. Un método para realizar ventas (utilice COLABORACIÓN) (2 Puntos)


from producto import Product
from abc import ABC, abstractmethod


class Tienda(ABC):
    @abstractmethod
    def ingress_products(self, name, cost, stock):
        pass

    @abstractmethod
    def list_products(self):
        pass

    @abstractmethod
    def sales(self, name_product, quantity):
        pass


class Restaurante(Tienda):
    def __init__(self, name, delivery_cost):
        self.__name = name
        self.__delivery_cost = delivery_cost
        self.__product_list = []
    
    def ingress_products(self, name:str, cost:int, stock:int = 0):
        p = Product(name, cost)
        encontrados = list(filter(lambda x : x.name == p.name, self.__product_list))
        if len(encontrados) == 0:
            self.__product_list.append(p)

    def list_products(self)-> str:
        if len(self.__product_list):
            retorno = ''

            for p in self.__product_list:
                retorno += f'Nombre: {p.name},\n'\
                            f'Precio: {p.cost}, \n'
            return retorno

        else:
            return 'no hay productos'
    
    def sales(self, product_name:str, cantidad:int):
        pass


class Farmacia(Tienda):
    def __init__(self, name, delivery_cost):
        self.__name = name
        self.__delivery_cost = delivery_cost
        self.__product_list = []
    
    def ingress_products(self, name:str, cost:int, stock:int = 0):
        p = Product(name, cost, stock)
        encontrados = list(filter(lambda x : x.name == p.name, self.__product_list))
        if len(encontrados) == 0:
            self.__product_list.append(p)
        else:
            indice = self.__product_list.index(encontrados[0])
            self.__product_list[indice].stock += stock

    def list_products(self)-> str:
        if len(self.__product_list):
            retorno = ''

            for p in self.__product_list:
                m = ''
                if p.cost > 15000:
                    m = 'envio gratis al solicitar el producto'
                retorno += f'Nombre: {p.name}, \n'\
                            f'Precio: {p.cost}, {m}\n'
            return retorno

        else:
            return 'no hay productos'
    
    def sales(self, product_name:str, cantidad:int):
        if cantidad < 3:
            p = Product(product_name, 0, cantidad)
            encontrados = list(filter(lambda x : x == p, self.__product_list))

            if len(encontrados) and encontrados[0].stock:
                tmp = encontrados[0] - p
                nuevo_stock = tmp if tmp > 0 else 0
                indice = self.__product_list.index(p)
                self.__product_list[indice].stock = nuevo_stock

        return 'venta realizada'

class Supermercado(Tienda):
    def __init__(self, name, delivery_cost):
        self.__name = name
        self.__delivery_cost = delivery_cost
        self.__product_list = []
    
    def ingress_products(self, name:str, cost:int, stock:int = 0):
        p = Product(name, cost, stock)
        encontrados = list(filter(lambda x : x.name == p.name, self.__product_list))
        if len(encontrados) == 0:
            self.__product_list.append(p)
        else:
            indice = self.__product_list.index(encontrados[0])
            self.__product_list[indice].stock += stock

    def list_products(self)-> str:
        if len(self.__product_list):
            retorno = ''

            for p in self.__product_list:
                m = ''
                if p.stock < 10:
                    m = 'pocos productos disponibles'
                retorno += f'Nombre: {p.name},\n'\
                            f'Precio: {p.cost},\n'\
                            f'Stock: {p.stock} {m}\n'
            return retorno

        else:
            return 'no hay productos'
    
    def sales(self, product_name:str, cantidad:int):

        p = Product(product_name, 0, cantidad)
        encontrados = list(filter(lambda x : x == p, self.__product_list))

        if len(encontrados) and encontrados[0].stock:
            tmp = encontrados[0] - p
            nuevo_stock = tmp if tmp > 0 else 0
            indice = self.__product_list.index(p)
            self.__product_list[indice].stock = nuevo_stock

        return 'venta realizada'

if __name__ == "__main__":
    tienda = Supermercado('tienda_name', 1000)
    tienda.ingress_products('nombre_producto', 120, 10)
    tienda.ingress_products('nombre_pr', 120000, 1)
    tienda.ingress_products('nombre_producto', 120, 3)
    print(tienda.list_products())