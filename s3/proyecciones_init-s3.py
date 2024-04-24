import numpy as np
import cv2

# Funciones
def draw(vertices, edges, im):
  """Dibuja objeto definido por vertices y bordes"""

  # Normalizar coordenadas homogeneas
  v_h = []
  for v in vertices:
    if v[-1] != 0:
      v_h.append(v[:-1]/v[-1])  

  for e in edges:
    x1 = np.where(np.isnan(vp[e[0]][0]), 0, vp[e[0]][0]) 
    y1 = np.where(np.isnan(vp[e[0]][1]), 0, vp[e[0]][1])

    x2 = np.where(np.isnan(vp[e[1]][0]), 0, vp[e[1]][0])
    y2 = np.where(np.isnan(vp[e[1]][1]), 0, vp[e[1]][1]) 

    cv2.line(im, (x1.astype(int), y1.astype(int)), 
         (x2.astype(int), y2.astype(int)),
         (255,0,15), 2)
  
  for v in v_h:
    cv2.circle(im, tuple(v.astype(int)), 3, (255,0,255),-1)

def translate3d(vertex, dx, dy, dz):
  """Operación de traslación 3d"""
  vertex[0] += dx
  vertex[1] += dy
  vertex[2] += dz
  return vertex

def project2D(vertex, f=200, w=500, h=500):
  """Aplica una transformacion de proyeccion pinhole"""
  eps = 1e-6
  x = vertex[0]*f/(vertex[2] + eps) + w/2
  y = vertex[1]*f/(vertex[2] + eps) + h/2
  return [x, y]

# Definir geometría del cubo
v = np.array([[0,0,0,1],[0,0,100,1],[100,0,100,1],[100,0,0,1],
             [100,100,0,1],[0,100,0,1],[0,100,100,1],[100,100,100,1]]) 

edges = [(0,1),(1,2),(2,3),(3,0),(0,4),(1,5),(2,6),(3,7),
         (4,5),(5,6),(6,7),(7,4),(0,7),(1,6)]

# Trasladar cubo         
dx, dy, dz = -50, -50, -100
for i in range(len(v)):
  v[i] = translate3d(v[i], dx, dy, dz)

# Proyectar vértices 
# Proyectar vértices  
vp = [project2D(v[i]) for i in range(len(v))]

# Filtrar vp 
vp = [v for v in vp if not np.any(np.isnan(v))]

# Dibujar y mostrar
im = np.zeros((500,500,3), np.uint8) 
draw(vp, edges, im)

cv2.imshow('imagen', im)
cv2.waitKey(0)