from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    def __init__(self,ancho: int, alto:int, url_archivo: str, url_clic:str, sub_tipo: str):
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = nuevo_ancho if nuevo_ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, nuevo_alto):
        self.__alto = nuevo_alto if nuevo_alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, nuevo_url_archivo):
        self.__url_archivo = nuevo_url_archivo

    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, nuevo_url_clic):
        self.__url_clic = nuevo_url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if isinstance(nuevo_sub_tipo, self.Video.SUB_TIPOS):
            self.__sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoError("error al ingresar Sub Tipo")

        
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos():
        return f'{sub_tipos}'\
                f'FORMATO {tipo.FORMATO}'\
                f'======================'\
                f'-{sub_tipo[0]}'\
                f'-{sub_tipo[1]}'


#funcion para delimitar duracion del video
def validar_duracion(duracion):
    if duracion > 0:
        return duracion
    else:
        return 5


class Video(Anuncio):
    FORMATO = 'Video'
    SUB_TIPOS = ('instream', 'outstream')
    
    def __init__(self,duracion):
        self.formato = Video.FORMATO
        self.__ancho = 1
        self.__alto = 1
        self.__duracion = validar_duracion(duracion)
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        print('No se puede modificar')

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, nuevo_alto):
        print('No se puede modificar')

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, nuevo_duracion):
        self.__duracion = validar_duracion(nuevo_duracion)
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = 'Display'
    SUB_TIPOS = ('tradicional', 'native')


    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = 'Social'
    SUB_TIPOS = ('facebook', 'linkedin')


    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")