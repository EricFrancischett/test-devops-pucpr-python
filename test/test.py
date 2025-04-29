from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=10000):
        result = await funcaoteste()
        assert result == {"teste": True, "num_aleatorio": 10000}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(nome="João", curso="Python", ativo=True)
    result = await create_estudante(estudante_teste)
    assert result == estudante_teste


@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result


@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result


@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result
