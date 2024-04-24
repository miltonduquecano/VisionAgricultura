import cv2
import numpy as np

W = 600
H = 200

im = np.zeros((H, W), np.uint8)

# Definir el número de líneas horizontales (y su frecuencia) basadas en la función seno
num_lines = 10
frequency = 20  # Frecuencia de la onda seno

# Dibujar las líneas horizontales que siguen una función seno
for i in range(num_lines):
    amplitude = int(H / (50))  # La amplitud de la línea varía con la frecuencia
    y_offset = H // (num_lines + 1) * (i + 1)
    
    # Generar puntos basados en la función seno
    x = np.arange(0, W)
    y = amplitude * np.sin(2 * np.pi * frequency * x / W) + y_offset
    
    # Convertir los puntos a enteros
    points = np.column_stack((x, y)).astype(np.int32)
    
    # Dibujar la línea
    cv2.polylines(im, [points], isClosed=False, color=255, thickness=1)

# Mostrar la imagen
cv2.imshow('window', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
