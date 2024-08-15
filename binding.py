import ctypes
import numpy as np

# Carregar a biblioteca C compilada
raytracing = ctypes.CDLL('./raytracing.so')

# Configurar o protótipo da função C
raytracing.render.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte)]
raytracing.render.restype = None

# Função Python para chamar a função C
def render_image(width, height):
    # Criar um array numpy para armazenar a imagem
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Chamar a função C para renderizar a imagem
    raytracing.render(width, height, image.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)))

    return image
