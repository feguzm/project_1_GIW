"""
TODO: rellenar

Asignatura: GIW
Práctica 1
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""


# Ejercicio 1

def dimension(matriz):
    filas = 0
    columnas = 0
    for x in matriz:
        filas += 1
        for y in matriz[x]:
            columnas += 1
    return (filas, columnas)

def es_cuadrada(matriz):
    ...

def es_simetrica(matriz):
    ...


def multiplica_escalar(matriz, k):
    ...

def suma(matriz1, matriz2):
    ...


# Ejercicio 2
def validar(grafo):
    ...

def grado_entrada(grafo, nodo):
    ...

def distancia(grafo, nodo):
    ...
   

#a partir de aquí está el código para probar las funciones
matriz1 = [[1, 0, 2, 5], 
           [0, 3, 3, 5], 
           [1, 2, 2, 5]]

matriz2 = [[1, 0, 1], 
           [0, 3, 2], 
           [1, 2, 2]]

print(dimension(matriz1))
