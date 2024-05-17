from anuncio import Anuncio, Video, Display, Social
from datetime import date
from error import LargoExcedidoError


# Se debe incluir en el constructor de la clase Campaña los parámetros y la lógica
# necesaria para instanciar dentro de él los anuncios a incorporar en el atributo que
# almacena el listado de anuncios. Como sugerencia, puede usar en el constructor un
# parámetro que sea una estructura de datos que contenga la información necesaria
# para crear cada instancia de Anuncio (por ejemplo, una tupla con diccionarios).
# Opcionalmente, puede refactorizar esta lógica específica en un método privado.


class Campaña():
    def __init__(self,nombre: str, fecha_inicio:date, fecha_termino:date, anuncios:tuple) -> None:
        self.__nombre = nombre
        self.__fecha_inicio: fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = self.anuncios_list(anuncios)

    def anuncios_list(self, anuncios:tuple) -> list:
        instancias = []
        for i, cantidad in enumerate(anuncios):
            for j in range(1, cantidad + 1):
                if i == 0:
                    instancias.append(Video(f'url_{j}', f'url_clic_{j}', 'instream', j))
                elif i == 1:
                    instancias.append(Display(j, j, f'url_{j}', f'url_clic_{j}', 'tradicional'))
                elif i == 2:
                    instancias.append(Social(j, j, f'url_{j}', f'url_clic_{j}', 'facebook'))
        return instancias

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) < 250:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoError("error al exceder el maximo de 250 caracteres del nombre")

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

        for anuncio in self.anuncios:
            if isinstance(anuncio, Video):
                video += 1
            elif isinstance(anuncio, Display):
                display += 1
            elif isinstance(anuncio, Social):
                social += 1
        
        return f'nombre de la campana : {self.nombre}'\
                f'\nanuncios: {video} Video, {display} Display, {social} Social'


if __name__ == "__main__":
    video_1 = Video('url', 'url_clic', 'instream', 3)
    campaña = Campaña('campaña1', date(2022, 5, 16), date(2024, 5, 16), (2,3,2))

    print(campaña.anuncios)
