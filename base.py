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

def amplitud_transicion (v4,v5):
    norma1= np.linalg.norm(v5)
    norma2 = np.linalg.norm(v4)
    ket_llegada = np.conjugate(np.transpose(v5))
    resultf3  = (np.dot(ket_llegada, v4))/ norma1 * norma2
    return resultf3


def media_varianza (observable, ket3, identidad):
    hermitiana = np.transpose(np.conjugate(observable))
    if (hermitiana == observable).all():
        operacion1 = np.dot(observable, ket3)
        operacion2 = np.transpose(np.conjugate(operacion1))
        operacion3 = np.dot(ket3, operacion2)
        def_matrix= np.dot(operacion3, identidad)
        operacion4 = observable - def_matrix
        oper_misma = np.dot(operacion4 , operacion4)
        def_estado = np.transpose(np.conjugate(ket3))
        operacion = np.dot(def_estado, oper_misma)
        operacion_final = np.dot(operacion, ket3)
        return operacion3, operacion_final
    else:
        print("El observable no es hermitiana")

def val_vecpropios (observable, estado):
    valores, vectores = np.linalg.eig(observable)
    normalizar = np.linalg.norm(vectores, axis=0)
    normalizados = vectores / normalizar
    transicion = np.abs(np.dot(normalizados.T.conj(), estado)) ** 2
    return valores, vectores, transicion


def dinamica (estado1,matriz1,matriz2):
    operacion1 = np.dot(matriz1, estado1)
    operacion2 = np.dot(matriz2, operacion1 )
    return operacion2


if __name__ == '__main__':

    v0 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
    v1 = np.array([complex(-3, -1), complex(0, -2), complex(0, 1), complex(2, 0)])
    p = 2
    print (probabilidad_position(v1, p))
    print("-"*15)
    v2 = np.array ([complex(2,1), complex(-1,2), complex(0,1), complex(1,0),complex(3,-1),complex(2,0),complex(0,-2),complex(-2,1),complex(1,-3),complex(0,-1)])
    v3 = np.array ([complex(-1,-4), complex(2,-3), complex(-7,6), complex(-1,1),complex(-5,-3),complex(5,0),complex(5,8),complex(4,-4),complex(8,-7),complex(2,-7)])
    print (probabilidad_transito (v2, v3))
    print("-" * 15)
    v4 = np.array([complex(2, 1), complex(-1, 2), complex(0, 1), complex(1, 0), complex(3, -1), complex(2, 0), complex(0, -2),complex(-2, 1), complex(1, -3), complex(0, -1)])
    v5 = np.array([complex(-1, -4), complex(2, -3), complex(-7, 6), complex(-1, 1), complex(-5, -3), complex(5, 0), complex(5, 8),complex(4, -4), complex(8, -7), complex(2, -7)])
    print(amplitud_transicion (v4,v5))
    print("-" * 15)
    observable = np.array([[complex(0, 0), complex(0, -1)], [complex(0, 1), complex(0, 0)]])
    ket3 = np.array([complex(1 / math.sqrt(2), 0), complex(0, 1 / math.sqrt(2))])
    identidad = np.array([[1, 0], [0, 1]])
    operacion3, operacion_final = media_varianza(observable, ket3, identidad)
    print("Resultado de la media:", operacion3)
    print("Resultado de la varianza:", operacion_final)
    print("-" * 15)
    observable = np.array([[complex(0, 0), complex(0, -1)], [complex(0, 1), complex(0, 0)]])
    estado = np.array([complex(1, 0), complex(0, 0)])
    valores, vectores, transicion = val_vecpropios(observable, estado)
    print("valores propios:", valores)
    print("vectores propios:", vectores)
    print("Probabilidad de transición:", transicion)
    print("-" * 15)
    estado1 = np.array([complex(1, 0), complex(0, 0)])
    matriz1 = np.array([complex(1, 0), complex(1, 1)])
    matriz2 = np.array([complex(1, 1), complex(1, 0)])
    print (dinamica (estado1,matriz1,matriz2))
    
