import pytest
from calculadora.operaciones import sumar, dividir, restar


@pytest.mark.suma
def test_sumar_positivos( numeros ):
    assert sumar(*numeros) == 12
    
@pytest.mark.suma
def test_sumar_negativos():
    assert sumar(-2,-6) == -8

@pytest.mark.parametrize("a,b,resultado",[
    (3,3,6),
    (5,15,20),
    (6,6,12)
],
ids=["caso1","caso2","caso3"]
)
def test_sumar_casos( a,b,resultado ):
    assert sumar(a,b) == resultado

