# En un archivo producto.py, definir la clase que permita instanciar productos.
# Considera para la definición de esta clase lo señalado en la descripción de la
# problemática (utilice ENCAPSULAMIENTO).


class Product():

    def __init__(self, name:str, cost:int, stock:int = 0):
        self.__name = name
        self.__cost = cost
        self.__stock = stock

    @property
    def name(self):
        return self.__name
    
    @property
    def cost(self):
        return self.__cost
    
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, cantidad:int):
        if cantidad < 0:
            self.__stock = 0
        else:
            self.__stock = cantidad


if __name__ == "__main__":
    p = Product('product_name', 120, 3)
    p.stock += 3
    print(p.stock)
