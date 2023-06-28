"""
Autor:kevin Andres Acosta Rengifo
fecha: 26/06/2023
Descripción: Archivo con los test necesarios para  saber
             si el codigo esta funcionando correctamente
"""

from lista_enlazada import ListaEnlazada
from combinar_listas_enlazadas import combinar


def test_lista_enlazada():
    objLista = ListaEnlazada()

    objLista.insertar(13)
    objLista.insertar(2)
    objLista.insertar(1)
    assert objLista.head.data == 13
    assert objLista.head.next.data == 2
    assert objLista.head.next.next.data == 1
    assert objLista.head.next.next.next is None


def test_get_index():
    objLista = ListaEnlazada()

    objLista.insertar(13)
    objLista.insertar(2)
    objLista.insertar(1)
    objLista.insertar(4)
    assert objLista.get_index(0) == 13
    assert objLista.get_index(1) == 2
    assert objLista.get_index(2) == 1
    assert objLista.get_index(3) == 4

    try:
        objLista.get_index(4)
    except IndexError:
        assert True
    else:
        assert False


def test_lenght():
    objLista = ListaEnlazada()

    objLista.insertar(13)
    objLista.insertar(2)
    assert objLista.lenght() == 2
    objLista.insertar(1)
    objLista.insertar(4)
    assert objLista.lenght() == 4
    objLista.insertar(4)
    assert objLista.lenght() == 5


def test_verificar_ordenada():
    lista = ListaEnlazada()
    lista1 = ListaEnlazada()
    lista.insertar(3)
    lista.insertar(7)
    lista.insertar(7)
    lista.insertar(9)
    assert lista.verificar_ordenada() is True
    lista.insertar(1)
    assert lista.verificar_ordenada() is False
    assert lista1.verificar_ordenada() is True


def test_combinar():
    lista1 = ListaEnlazada()
    lista2 = ListaEnlazada()
    # lista1 3, 7 ,9
    lista1.insertar(3)
    lista1.insertar(7)
    lista1.insertar(9)
    # lista2 1, 3, 8
    lista2.insertar(1)
    lista2.insertar(3)
    lista2.insertar(8)
    listaCombinada = combinar(lista1, lista2)
    # listaCombinada 1, 3, 3, 7, 8, 9
    assert listaCombinada.get_index(0) == 1
    assert listaCombinada.get_index(1) == 3
    assert listaCombinada.get_index(2) == 3
    assert listaCombinada.get_index(3) == 7
    assert listaCombinada.get_index(4) == 8
    assert listaCombinada.get_index(5) == 9

    # prueba 2
    lista3 = ListaEnlazada()
    lista4 = ListaEnlazada()
    # lista1 1, 3, 5, 7
    lista3.insertar(1)
    lista3.insertar(3)
    lista3.insertar(5)
    lista3.insertar(7)
    # lista2 2, 4, 6, 8
    lista4.insertar(2)
    lista4.insertar(4)
    lista4.insertar(6)
    lista4.insertar(8)
    listaCombinada2 = combinar(lista3, lista4)
    # listaCombinada 1, 2, 3, 4, 5, 6, 7, 8
    assert listaCombinada2.get_index(0) == 1
    assert listaCombinada2.get_index(1) == 2
    assert listaCombinada2.get_index(2) == 3
    assert listaCombinada2.get_index(3) == 4
    assert listaCombinada2.get_index(4) == 5
    assert listaCombinada2.get_index(5) == 6
    assert listaCombinada2.get_index(6) == 7
    assert listaCombinada2.get_index(7) == 8
    # prueba 3
    lista5 = ListaEnlazada()
    lista6 = ListaEnlazada()
    # lista1 3, 4, 5, 7, 10
    lista5.insertar(3)
    lista5.insertar(4)
    lista5.insertar(5)
    lista5.insertar(7)
    lista5.insertar(10)
    # lista2 1, 3, 6, 8, 9
    lista6.insertar(1)
    lista6.insertar(3)
    lista6.insertar(6)
    lista6.insertar(8)
    lista6.insertar(9)
    listaCombinada3 = combinar(lista5, lista6)
    # listaCombinada 1, 3, 3, 4, 5, 6, 7, 8, 9, 10
    assert listaCombinada3.get_index(0) == 1
    assert listaCombinada3.get_index(1) == 3
    assert listaCombinada3.get_index(2) == 3
    assert listaCombinada3.get_index(3) == 4
    assert listaCombinada3.get_index(4) == 5
    assert listaCombinada3.get_index(5) == 6
    assert listaCombinada3.get_index(6) == 7
    assert listaCombinada3.get_index(7) == 8
    assert listaCombinada3.get_index(8) == 9
    assert listaCombinada3.get_index(9) == 10

    # prueba 4
    lista7 = ListaEnlazada()
    lista8 = ListaEnlazada()
    # listas vacias
    listaCombinada4 = combinar(lista7, lista8)
    # listaCombinada vacia
    assert listaCombinada4.head is None

    # prueba 5
    lista9 = ListaEnlazada()
    lista10 = ListaEnlazada()
    # una lista vacía
    lista9.insertar(1)
    lista9.insertar(3)
    lista9.insertar(5)
    listaCombinada5 = combinar(lista9, lista10)
    assert listaCombinada5.get_index(0) == 1
    assert listaCombinada5.get_index(1) == 3
    assert listaCombinada5.get_index(2) == 5

    # prueba 6
    # una lista desordenada
    lista11 = ListaEnlazada()
    lista12 = ListaEnlazada()
    # lista11 1, 3, 5
    lista11.insertar(1)
    lista11.insertar(3)
    lista11.insertar(5)
    # lista12 2, 6, 1
    lista12.insertar(2)
    lista12.insertar(6)
    lista12.insertar(1)
    try:
        listaCombinada6 = combinar(lista11, lista12)
        listaCombinada6.get_index(0)
    except ValueError:
        assert True
    except Exception:
        assert False

