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

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_delivery_cost(self):
        return self.__delivery_cost
    
    def ingress_products(self, product_name:str, product_cost:int, product_stock:int = 0):
        for product in self.__product_list:
            print(product.get_name)
            if product.get_name == product_name:
                product.set_stock += product_stock
                return
        p = Product(product_name, product_cost, product_stock)
        self.__product_list.append(p)

    def list_products(self)-> str:
        products_info = ""
        for product in self.__product_list:
            products_info += f"Name: {product.get_name}, Cost: {product.get_cost}, Stock: {product.get_stock}\n"
        return products_info
    
    def sales(self, product_name:str, cantidad:int):
        for product in self.__product_list:
            if product.get_name == product_name:
                current_stock = product.get_stock
                if current_stock >= cantidad:
                    product.set_stock(current_stock - cantidad)
                    print(f"{cantidad} {product_name} sold successfully.")
                else:
                    print(f"Not enough stock for {cantidad} {product_name}.")
                return
        print(f"{product_name} not found in the product list.")


class Farmacia(Tienda):
    pass

class Supermercado(Tienda):
    pass

if __name__ == "__main__":
    tienda = Restaurante('tienda_name', 1000)
    tienda.ingress_products('nombre_producto', 120, 3)
    tienda.ingress_products('nombre_pr', 120, 1)
    tienda.ingress_products('nombre_producto', 120, 3)
    print(tienda.list_products())