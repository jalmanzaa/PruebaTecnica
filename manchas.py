import cv2
import numpy as np

def estimate_area(img, n_samples):
    height, width = img.shape
    # Generar coordenadas aleatorias dentro de la imagen
    rand_x = np.random.randint(0, width, n_samples)
    rand_y = np.random.randint(0, height, n_samples)
    # Contar cuántos puntos aleatorios caen dentro de la mancha
    n_inside = np.sum(img[rand_y, rand_x])
    # Estimar el área de la mancha
    area = n_inside / n_samples * height * width
    return area

# Cargar imagen binaria
img = cv2.imread('mancha.png', cv2.IMREAD_GRAYSCALE)
# Calcular el área estimada de la mancha
area_estimada = estimate_area(img, 10000)
print('Área estimada de la mancha: {area_estimada} píxeles cuadrados')