import pytest


@pytest.fixture
def numeros():
    return 10,2

@pytest.fixture
def numeros_por_cero():
    return 10,0