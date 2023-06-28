"""
Autor: Kevin Andres Acosta Rengifo
fecha: 25/06/2023
Descripción: Clase que representa un nodo de la lista enlazada
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None