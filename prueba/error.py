class Error(Exception):
    pass


class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f'{self.mensaje}'\


class SubTipoInvalidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f'{self.mensaje}'
