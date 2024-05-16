class Error(Exception):
    pass


class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f'mensaje de error:{self.mensaje},'\


class SubTipoInvalidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f'mensaje de error:{self.mensaje},'
