# Importar librerías necesarias
import random
import cv2

# Cargar la imagen que contiene la mancha
img = cv2.imread('D:\Python\PruebaTecnica\mancha.jpg', 0)

# Definir el número de puntos aleatorios a generar
n = 10000

# Definir un contador para los puntos que caen dentro de la mancha
ni = 0

# Obtener las dimensiones de la imagen
h, w = img.shape

# Generar n puntos aleatorios uniformemente distribuidos dentro de la imagen
for i in range(n):
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)

    # Verificar si el punto aleatorio está dentro de la mancha
    if img[y,x] == 255: # o cualquier valor que corresponda a la mancha
        ni += 1

# Calcular la superficie estimada de la mancha
S_estimada = (ni/n) * w * h

# Mostrar el resultado
print("La superficie estimada de la mancha es:", S_estimada)