import pytest
from arquivo2 import funcao_calcular_pedido
def test_total_somente_um_produto():
    assert funcao_calcular_pedido ([100]) == 9.0
def test_total_varios_produtos():
    assert funcao_calcular_pedido ([100, 101, 105, 201]) == 41.0
def test_total_produto_invalido():
    assert funcao_calcular_pedido ([200, 300, 104]) == 19.0
def test_total_sem_produto():
    assert funcao_calcular_pedido ([]) == 0.0
def test_total_produtos_repetidos():
    assert funcao_calcular_pedido ([100, 100, 105, 200, 201, 201]) == 48.0
def test_total_todos_produtos():
    assert funcao_calcular_pedido ([100, 101, 102, 103, 104, 105, 200, 201]) == 84.0
def test_total_produto_inexistente():
    funcao_calcular_pedido ([300]) == 0.0