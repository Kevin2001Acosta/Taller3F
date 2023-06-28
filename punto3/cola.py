"""
Autor: Kevin Andres Acosta Rengifo
fecha: 28/06/2023
Descripción: Clase que representa una cola
"""
import numpy as np


class Cola:

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