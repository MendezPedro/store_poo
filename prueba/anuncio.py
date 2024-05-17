from abc import ABC, abstractmethod
from error import SubTipoInvalidoError


class Anuncio(ABC):
    def __init__(self,ancho: int, alto:int, url_archivo: str, url_clic:str, sub_tipo: str):
        self.__ancho = validar_duracion(ancho,1)
        self.__alto = validar_duracion(alto,1)
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = validar_duracion(nuevo_ancho,1)

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, nuevo_alto):
        self.__alto = validar_duracion(nuevo_alto,1)

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
        # if isinstance(nuevo_sub_tipo, self.SUB_TIPOS):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self.__sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoError(f"error al ingresar Sub Tipo. Tipos permitidos{self.SUB_TIPOS}")

        
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos():
        return f'\nFORMATO 1: {Video.FORMATO}\tFORMATO 2: {Display.FORMATO}\tFORMATO 3: {Social.FORMATO}'\
                f'\n==================\t==================\t=================='\
                f'\n-{Video.SUB_TIPOS[0]}\t\t-{Display.SUB_TIPOS[0]}\t\t-{Social.SUB_TIPOS[0]}'\
            f'\n-{Video.SUB_TIPOS[1]}\t\t-{Display.SUB_TIPOS[1]}\t\t\t-{Social.SUB_TIPOS[1]}\n'


class Video(Anuncio):
    FORMATO = 'Video'
    SUB_TIPOS = ('instream', 'outstream')
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(ancho=1, alto=1, url_archivo=url_archivo, url_clic=url_clic, sub_tipo=sub_tipo)
        self.formato = Video.FORMATO
        self.__duracion = validar_duracion(duracion, 5)
        # si no lo vuelvo a declarar no me permite acceder
        self.__ancho = 1
        self.__alto = 1
    
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
        self.__duracion = validar_duracion(nuevo_duracion,5)
    
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


validar_duracion = lambda duracion, valor: duracion if duracion > 0 else valor

if __name__ == "__main__":
    video = Video('url', 'url_clic', 'instream', 3)
    # print(video.mostrar_formatos())
    print(validar_duracion(-3,1))

    # video.redimensionar_anuncio()
    print(video.ancho)
    video.ancho = 2
    print(video.ancho)