"""
Autor: Kevin Andres Acosta Rengifo
fecha: 26/06/2023
Descripción: crear una funcion que realize la combinacion de dos listas enlazadas
ordenadas y devuelve una lista enlazada ordenada
"""
from lista_enlazada import ListaEnlazada


def combinar(lista1, lista2):
    # primero preguntamos si las listas estan ordenandas
    if not lista1.verificar_ordenada() and not lista2.verificar_ordenada():
        raise ValueError("Las listas deben estar ordenadas")
    listaCombinada = ListaEnlazada()
    i = 0
    j = 0
    while i < lista1.lenght() and j < lista2.lenght():
        if lista1.get_index(i) < lista2.get_index(j):
            listaCombinada.insertar(lista1.get_index(i))
            i += 1

        else:
            listaCombinada.insertar(lista2.get_index(j))
            j += 1

    while i < lista1.lenght():
        listaCombinada.insertar(lista1.get_index(i))
        i += 1

    while j < lista2.lenght():
        listaCombinada.insertar(lista2.get_index(j))
        j += 1

    return listaCombinada
