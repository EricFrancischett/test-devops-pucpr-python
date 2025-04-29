from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', return_value=10000):
        result = funcaoteste()
        yield result
        assert result == {"teste": True, "num_aleatorio": 10000}


def test_create_estudante():
    estudante_teste = Estudante(nome="João", curso="Python", ativo=True)
    result = create_estudante(estudante_teste)
    yield result
    assert result == estudante_teste


def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result


def test_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result


def test_delete_estudante_positivo():
    result = delete_estudante(10)
    yield result
    assert result
