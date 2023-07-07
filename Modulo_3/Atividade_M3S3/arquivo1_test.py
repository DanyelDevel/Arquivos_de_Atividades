import pytest
from arquivo1 import funcao_calculo_desconto

def test_funcao_inferior_de_10():
    assert funcao_calculo_desconto(10.0,5) ==(50.0,50.0)
def test_funcao_de_10_a_99():
    assert funcao_calculo_desconto(10.0, 50) == (500.0, 475.0)
def test_funcao_de_100_a_999():
    assert funcao_calculo_desconto(10.0, 999) == (9990.0, 8991.0)
def test_funcao_maior_a_999():   
    assert funcao_calculo_desconto(10.0, 1000) == (10000.0, 8500.0)
def test_funcao_limite_32():
    assert funcao_calculo_desconto(10.0, 2147483647) == (21474836470.0, 18253610999.5)  # Testa valor máximo de quantidade (para int32)


