"""
Autores:Kevin Acosta
         Ronan Moreno
         Rodolfo Bolaños
fecha: 27/06/2023
Descripción: Archivo de test para hacer las pruebas del inventario del museo
"""

import pytest
from obra import Node
from obra import Obra
from obra import LinkedListObra
from museo import Museo


def test_agregarReplica():
    museo = Museo()

    museo.agregarReplica("Gioconda")
    museo.agregarReplica("Gioconda")
    museo.agregarReplica("Gioconda")
    assert museo.inventario.head.value.nombre == "Gioconda"
    assert museo.inventario.head.value.cantidad == 3

    museo.agregarReplica("Persistencia de la memoria")
    museo.agregarReplica("Persistencia de la memoria")
    assert museo.inventario.head.ptrNext.value.nombre == "Persistencia de la memoria"
    assert museo.inventario.head.ptrNext.value.cantidad == 2


def test_venderReplica():
    museo = Museo()

    museo.agregarReplica("Gioconda")
    museo.agregarReplica("Persistencia de la memoria")

    museo.venderReplica("Gioconda")
    assert museo.inventario.head.value.nombre == "Persistencia de la memoria"
    assert museo.inventario.head.value.cantidad == 1

    # museo.venderReplica("Persistencia de la memoria")
    # with pytest.raises(ReferenceError):
    #     museo.inventario.getIndex(0)

    # try:
    #     museo.venderReplica("Obra inexistente")
    # except ReferenceError:
    #     assert True
    # except Exception:
    #     assert False


def test_listarReplicas(capsys):
    museo = Museo()

    museo.agregarReplica("Gioconda")
    museo.agregarReplica("Gioconda")
    museo.agregarReplica("Gioconda")
    museo.venderReplica("Gioconda")
    museo.agregarReplica("Persistencia de la memoria")
    museo.venderReplica("Gioconda")

    museo.listarReplicas()

    captured = capsys.readouterr()
    expected_output = "Obra: Gioconda, Cantidad: 1\nObra: Persistencia de la memoria, Cantidad: 1\n"
    assert captured.out == expected_output
