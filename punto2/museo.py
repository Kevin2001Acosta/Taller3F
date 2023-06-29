"""
Autor: Rodolfo Bolanos
fecha: 27/06/2023
Descripción: Clase museo y sus metodos
"""


from obra import Node
from obra import Obra
from obra import LinkedListObra

class Museo:
    def __init__(self):
        self.inventario = LinkedListObra()

    def agregarReplica(self, nombre):
        current = self.inventario.head
        while current is not None:
            if current.value.nombre == nombre:
                current.value.cantidad += 1
                return
            current = current.ptrNext

        obra = Obra(nombre, 1)
        self.inventario.insert(obra)

    def venderReplica(self, nombre):
        current = self.inventario.head
        while current is not None:
            if current.value.nombre == nombre:
                if current.value.cantidad > 0:
                    current.value.cantidad -= 1
                    if current.value.cantidad == 0:
                        self.inventario.delete(current.value)
                    return
                else:
                    print("No hay obras disponibles con el nombre especificado.")
                    return
            current = current.ptrNext

    def listarReplicas(self):
        self.inventario.listarReplicas()