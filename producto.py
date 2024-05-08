# En un archivo producto.py, definir la clase que permita instanciar productos.
# Considera para la definición de esta clase lo señalado en la descripción de la
# problemática (utilice ENCAPSULAMIENTO).


class Product():

    def __init__(self, name:str, cost:int, stock:int = 0):
        self.__name = name
        self.__cost = cost
        self.__stock = stock

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_cost(self):
        return self.__cost
    
    @property
    def get_stock(self):
        return self.__stock
    
    @get_stock.setter
    def set_stock(self, cantidad:int):
        if cantidad < 0:
            self.__stock = 0
        else:
            self.__stock = cantidad


if __name__ == "__main__":
    p = Product('product_name', 120, 3)
    p.set_stock += 3
    print(p.get_stock)
