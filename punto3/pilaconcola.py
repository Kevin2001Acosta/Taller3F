"""
Autores: Kevin Acosta
         Ronan Moreno
         Rodolfo Bolaños
Fecha: 28/06/2023
Descripción: Clase que representa una cola
"""
import numpy as np


class PilaConCola:

    def __init__(self, n):
        self.size = 0
        self.queue = np.zeros(n)
        self.head = 1
        self.tail = 1
        self.n = n

    def enqueue(self, value):
        if self.tail == self.head and self.size > 0:
            raise NotImplementedError("La cola esta llena")
        else:
            self.size += 1
            self.queue[self.tail - 1] = value
            if self.tail == self.n:
                self.tail = 1
            else:
                self.tail += 1

    def dequeue(self):
        if self.tail == self.head and self.size == 0:
            raise NotImplementedError("La cola esta vacia")
        else:
            self.size -= 1
            val = self.queue[self.head - 1]
            if self.head == self.n:
                self.head = 1
            else:
                self.head += 1

        return val

    """"
    las lienas siguientes se implementan funciones que individualmente funcionan 
    como pila en esta cola osea si encolamos y hacemos pop el ultimo que entre es 
    el primero que sale
    
    si hacemos push y desencolamos el primero que entre es el ultimo que sale
    """

    def estaVaciaPilaConColas(self):
        if self.size == 0:
            return True
        else:
            return False

    def pushPilaConColas(self, value):
        if self.tail == self.head and self.size > 0:
            raise NotImplementedError("La cola esta llena")
        else:
            self.size += 1
            # por la estructura de los array de numpy puedo poner
            # el valor en la pos -1 que sería igual
            # a la ultima posicion cuando la cabeza esté al principio
            self.queue[self.head - 2] = value  # agrega el valor antes de la cabeza
            if self.head == 1:   # con este condicional pongo al head en la posicion del valor
                self.head = self.n
            else:
                self.head -= 1

    def popPilaConColas(self):
        # elimino el ultimo que ingresó
        if self.tail == self.head and self.size == 0:
            raise NotImplementedError("La cola esta vacia")
        else:
            self.size -= 1
            val = self.queue[self.tail - 2]
            if self.tail == 1:
                self.tail = self.n
            else:
                self.tail -= 1

        return val
    """
    mostraremos la pila con colas como se mostraría una lista
    """
    def mostrarPilaConColas(self):
        if self.tail == self.head and self.size == 0:
            print("[]")
        else:
            if self.tail > self.head:
                print("[")
                for i in range(self.head - 1, self.tail - 1):
                    print(self.queue[i], end=" ")
                print("]")
            else:
                print("[")
                for i in range(self.head - 1, self.n):
                    print(self.queue[i], end=" ")
                for i in range(0, self.tail - 1):
                    print(self.queue[i], end=" ")
                print("]")
            print()