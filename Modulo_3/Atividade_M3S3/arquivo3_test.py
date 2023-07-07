from arquivo3 import validar_medida, \
                calcular_preco_volume, \
                calcular_multiplicador_peso, \
                calcular_multiplicador_rota, \
                calcular_frete
import pytest
def tes_medida_numero():
    assert validar_medida('5') == 5
def test_medida_nao_numerica():
    assert validar_medida('abc') == -1
def test_preco_volume_menor_1000():
    assert calcular_preco_volume(500) == 10.0
def test_preco_volume_1000_10000():
    assert calcular_preco_volume(5000) == 20.0
def test_preco_volume_10000_30000():
    assert calcular_preco_volume(15000) == 30.0
def test_preco_volume_30000_100000():
    assert calcular_preco_volume(50000) == 20.0
def test_preco_volume_maior_100000():
    assert calcular_preco_volume(150000) == 0.0
def test_multiplicador_peso_50g():
    assert calcular_multiplicador_peso(0.05) == 1.0  
def test_multiplicador_peso_500g():
    assert calcular_multiplicador_peso(0.5) == 1.5  
def test_multiplicador_peso_5kg():
    assert calcular_multiplicador_peso(5) == 2.0
def test_multiplicador_peso_20kg():
    assert calcular_multiplicador_peso(20) == 3.0  
def test_multiplicador_peso_31kg():
    assert calcular_multiplicador_peso(31) == 0
def test_multiplicador_rota_br():
    assert calcular_multiplicador_rota('br') == 1.5 
def test_multiplicador_rota_rs():
    assert calcular_multiplicador_rota('rs') == 1.0
def test_multiplicador_rota_SB():
    assert calcular_multiplicador_rota('SB') == 1.2
def test_multiplicador_rota_zz():
    assert calcular_multiplicador_rota('zz') == 0
def test__frete():
    assert calcular_frete(1000, 1.5, 1.0) == 1500
    assert calcular_frete(2000, 2.0, 1.2) == 4800
    assert calcular_frete(5000, 3.0, 1.5) == 22500
