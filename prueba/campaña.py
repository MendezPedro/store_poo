from anuncio import Anuncio
from datetime import date
from error import LargoExcedidoError


class Campaña():
    def __init__(self,nombre: str, fecha_inicio:date, fecha_termino:date, anuncios:Anuncio) -> None:
        self.__nombre = nombre
        self.__fecha_inicio: fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [anuncios]

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) < 250:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoError("error al exceder los caracteres del nombre (250)")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, nuevo_fecha_inicio):
        self.__fecha_inicio = nuevo_fecha_inicio

    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, nuevo_fecha_termino):
        self.__fecha_termino = nuevo_fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        video = 0
        display = 0
        social = 0

        for anuncio in anuncios:
            if isinstance(anuncio, Video):
                video += 1
            elif isinstance(anuncio, Display):
                display += 1
            elif isinstance(anuncio, Social):
                social += 1
        
        return f'nombre de la campana : {self.nombre}'\
                f'anuncios: {video} Video, {display} Display, {social} Social'
    
    







