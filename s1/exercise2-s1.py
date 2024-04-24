import cv2
import numpy as np

# Dimensiones de la imagen
W = 200
H = 200

# Crear una imagen en blanco
im = np.zeros((W, H, 3), np.uint8)

# Definir los colores
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Dibujar los cuadrados
for i, color in enumerate(colors):
    # Calcular el tamaño del cuadrado
    size = (i + 1) * 20
    
    # Calcular las coordenadas del cuadrado
    start = (W // 2 - size // 2, H // 2 - size // 2)
    end = (W // 2 + size // 2, H // 2 + size // 2)
    
    # Dibujar el cuadrado
    cv2.rectangle(im, start, end, color, 10)

# Mostrar la imagen
cv2.imshow('window', im)
cv2.waitKey(0)
cv2.destroyAllWindows()