class Error(Exception):
    pass


class LargoExcedidoError(Error):
    def __init__(self, mensaje, dimension: int = None, maximo: int = None):
        self.dimension = dimension
        self.maximo = maximo
        self.mensaje = mensaje

    def __str__(self) -> str:
        if self.mensaje and self.dimension is None and self.dimension is None:
            return super().__str__()
        else:
            return f'mensaje de error:{self.mensaje},'\
                    f'dimension:{self.dimension},'\
                    f'maximo:{self.maximo}'


class SubTipoInvalidoError(Error):
    def __init__(self, mensaje, dimension: int = None, maximo: int = None):
        self.dimension = dimension
        self.maximo = maximo
        self.mensaje = mensaje

    def __str__(self) -> str:
        if self.mensaje and self.dimension is None and self.dimension is None:
            return super().__str__()
        else:
            return f'mensaje de error:{self.mensaje},'\
                    f'dimension:{self.dimension},'\
                    f'maximo:{self.maximo}'
        