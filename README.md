# Números complejos

## Libreria NUMPY
La libreria Numpy también pronunciada Numpai es una biblioteca de lenguaje natural de Python, el cuál da soporte a la 
creación de vectores y matrices, junto a estas, una serie de operadores matemáticos

## Libreria MATH
la libreria Math es una biblioteca de lenguaje natural Python, da al usuario la disposición y uso de las operaciones algebraicas

## ¿Qué es Pycharm y para que sirve?
Pycharm es el IDE más popular para el lenguaje de programación python.

## Como instalar la libreria numpy en Pycharm
Para poder descargar la libreria debemos hacer los siguientes pasos:
	
    - Abrir Pychar y crear un nuevo documento.
	- Vamos al aportado de "File" y luego a la opción de "New projects settings"
	- Se desplegará una ventana y daremos click en "Project interpreter", damos clic en la flecha donde dice 
		"Add interpreter"
	- Buscaremos el nombre de nuestro proyecto y daremos click.
	- En la parte superior izquierda aparecerá un + le daremos click y en la barra buscaremos "Numpy"
	- Daremos click y luego en la parte inferior derecha un boton en verde que dice "Add package"
	- Esperaremos que cargue y listo ya quedó la libreria instalada en nuestro entorno de programación.
	- Para importar la función escribimos "import Numpy as np" y podremos disponer de la funciones de la libreria.

## Como instalar la libreria math en Pycharm
Para poder descargar la libreria debemos hacer los siguientes pasos:
	
    - Abrir Pychar y crear un nuevo documento.
	- Vamos al aportado de "File" y luego a la opción de "New projects settings"
	- Se desplegará una ventana y daremos click en "Project interpreter", damos clic en la flecha donde dice 
		"Add interpreter"
	- Buscaremos el nombre de nuestro proyecto y daremos click.
	- En la parte superior izquierda aparecerá un + le daremos click y en la barra buscaremos "math lab"
	- Daremos click y luego en la parte inferior derecha un boton en verde que dice "Add package"
	- Esperaremos que cargue y listo ya quedó la libreria instalada en nuestro entorno de programación.
	- Para importar la función escribimos "import math " y podremos disponer de la funciones de la libreria.

## Función "Complex" en python.
La función complex devuelve un número imaginario a partir de valores cedidios como argumentos.
La parte derecha de nuestro argumento se interpreta como parte imaginaria.
tupla (a,b) -> (a, bj)
 
# Función #1
El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
- Definimos el vector V1
- Definimos la posición donde queremos encontrar la posibilidad.
- Mediante la función "np.linalg.norm(v1)" propia de Nuympy encontramos la norma del vector.
- Definimos la posición como la variable "p"
- Para encontrar el valor en esa posición utilizamos v1[p]
- Definimos la operación como el valor absoluto de la posición elevado al cuadrado sobre la norma del vector al cuadrado.

# Función #2
El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
- Definimos el vector V2
- Definimos el vector V3
- Encontramos el Bra del ket de llegada, utilizamos las funciones propias de Numpy "np.transpose(np.conjugate(v3))"
- Definimos nuevamente nuestros vectores como Vector / norma del vector  (La norma del vector se puede encontrar con la función propia de Numpy np.linalg.norm(v))
- Definimos la operación como el producto interno entre el vector al que le encontramos el Bra y el vector de salida"

## Como se deben ejecutar las pruebas.
Las pruebas se deben ejecetar primero llamando la libreria unitest, a partir de ahi seguimos el procedimiento de llamar 
nuesta función de la libreria pasada. a partir de ahi definimos nuestras variables a utilizar y el valor que deseamos 
esperar, definimos la operación y al final citamos "np.testing.assert_almost_equal (operación, valor esperado)"
