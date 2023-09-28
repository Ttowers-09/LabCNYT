"""
ESCUELA COLOMBIANA DE INGENIERIA JULIO GARAVITO
Estudiante: Ivan Santiago F. Torres
Docente: Luis Daniel Benavides
Asignatura: CNYT

"""
import numpy as np
import math
def probabilidad_position(v1, p):
    norma = np.linalg.norm(v1)
    "Mediante la libreria Numpy podemos encontrar la norma mediante np.linalg.norm"
    posicion = v1[p]
    resultf = abs(posicion)**2 / (norma)**2
    return resultf

def probabilidad_transito (v2, v3):
    v3 = np.transpose(np.conjugate(v3))
    v3 = v3 / np.linalg.norm(v3)
    v2 = v2 / np.linalg.norm(v2)
    resultf2 = np.dot( v3, v2)
    return resultf2




if __name__ == '__main__':
    v0 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
    v1 = np.array([complex(-3, -1), complex(0, -2), complex(0, 1), complex(2, 0)])
    p = 2
    print (probabilidad_position(v1, p))
    v2 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
    v3 = np.array ([complex(-1,-4), complex(2,-3), complex(-7,6), complex(-1,1),complex(-5,-3),complex(5,0),complex(5,8),complex(4,-4),complex(8,-7),complex(2,-7)])

    v8 = np.array ([1,0,0,0,0,0,0,0,0,0])
    v9 = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    print (probabilidad_transito (v2, v3))
