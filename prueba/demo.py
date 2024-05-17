from campaña import Campaña
from anuncio import Video
from datetime import date
# with open("error.log", "w") as file:
#     pass

try:
    video_1 = Video('url', 'url_clic', 'instream', 3)
    campaña = Campaña('campaña1', date(2022, 5, 16), date(2024, 5, 16), video_1)
    nuevo_nombre = input("ingrese un nuevo Nombre para la campaña: ")
    campaña.nombre = nuevo_nombre
    nuevo_sub_tipo = input("ingrese un nuevo sub_tipo para la campaña: ")
    campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

except Exception as e:
    print(f"ERROR: {e}")
    with open("error.log", "a") as error_file:
        error_file.write(str(e) + '\n')

# print(campaña.nombre)
# print(campaña.anuncios[0].sub_tipo)