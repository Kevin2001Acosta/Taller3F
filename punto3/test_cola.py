"""
Autores: Kevin Acosta
         Ronan Moreno
         Rodolfo Bolaños
fecha: 28/06/2023
Descripción: archivo de tests para la clase PilaConCola
en esta implementaremos funciones inddividuales que se comportan
"""
from pilaconcola import PilaConCola


def test_enqueue_and_dequeue():
    cola = PilaConCola(5)
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
    assert cola.dequeue() == 1
    assert cola.dequeue() == 2
    assert cola.dequeue() == 3
    assert cola.dequeue() == 4
    assert cola.dequeue() == 5
    try:
        cola.dequeue()
    except NotImplementedError:  # La cola esta vacia
        assert True
    else:
        assert False


def test_estaVaciaPilaConColas():
    cola = PilaConCola(5)
    assert cola.estaVaciaPilaConColas() is True
    cola.enqueue(1)
    assert cola.estaVaciaPilaConColas() is False
    cola.dequeue()
    assert cola.estaVaciaPilaConColas() is True


def test_pushPilaConColas():
    # con push se ponen los valores atrás de la cabeza
    # y luego se actualiza la cabeza así cuando los saque
    # sacaré el último valor que entró con dequeue
    cola = PilaConCola(5)
    cola.enqueue(1)
    cola.pushPilaConColas(3)
    cola.pushPilaConColas(3)
    cola.pushPilaConColas(6)    # ultimo en entrar

    assert cola.dequeue() == 6  # primero en salir
    assert cola.dequeue() == 3
    assert cola.dequeue() == 3
    assert cola.dequeue() == 1


def test_popPilaConColas():
    cola = PilaConCola(5)
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    cola.enqueue(4)
    cola.enqueue(5)  # ultimo en entrar

    assert cola.popPilaConColas() == 5  # primero en salir
    assert cola.popPilaConColas() == 4
    assert cola.popPilaConColas() == 3
    assert cola.popPilaConColas() == 2
    assert cola.popPilaConColas() == 1
    try:
        cola.popPilaConColas()
    except NotImplementedError:  # La cola esta vacia
        assert True
    else:
        assert False


def test_mostrarPilaConColas():
    cola = PilaConCola(5)
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    cola.enqueue(4)
    cola.enqueue(5)  # ultimo en entrar
    cola.mostrarPilaConColas()

    cola1 = PilaConCola(5)
    cola1.pushPilaConColas(1)
    cola1.pushPilaConColas(2)
    cola1.pushPilaConColas(3)
    cola1.pushPilaConColas(4)
    cola1.pushPilaConColas(5)
    cola1.mostrarPilaConColas()





