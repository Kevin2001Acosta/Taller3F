"""
Autores: Kevin Acosta
         Ronan Moreno
         Rodolfo Bolaños
fecha: 28/06/2023
Descripción: archivo de tests para la clase Cola
"""
from cola import Cola


def test_enqueue_and_dequeue():
    cola = Cola(5)
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    cola.enqueue(4)
    cola.enqueue(5)
    try:
        cola.enqueue(6)
    except NotImplementedError:  # La cola esta llena
        assert True
    else:
        assert False
    assert cola.dequeue == 1
    assert cola.dequeue == 2
    assert cola.dequeue == 3
    assert cola.dequeue == 4
    assert cola.dequeue == 5
    try:
        cola.dequeue
    except NotImplementedError:  # La cola esta vacia
        assert True
    else:
        assert False