from campaña import Campaña
from anuncio import Video
# with open("error.log", "w") as file:
#     pass

try:
    video = Video()
    campaña = Campaña(anuncios[Video])
    nuevo_nombre = input("ingrese un nuevo Nombre para la campaña")
    nuevo_sub_tipo = input("ingrese un nuevo sub_tipo para la campaña")

except Exception as e:
    # print(f"ERROR: {e}")
    with open("error.log", "a") as error_file:
        error_file.write(str(e) + '\n')

