import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from app import app


@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente


def test_listar_fotos_retorna_200(cliente):
    resposta = cliente.get('/fotos')
    assert resposta.status_code == 200


def test_estrutura_json_das_fotos(cliente):
    resposta = cliente.get('/fotos')
    dados = resposta.get_json()
    assert 'fotos' in dados
    assert 'total' in dados
    primeira_foto = dados['fotos'][0]
    campos = ['id', 'titulo', 'autor', 'likes', 'data_publicacao', 'categoria']
    for campo in campos:
        assert campo in primeira_foto


def test_foto_inexistente_retorna_404(cliente):
    resposta = cliente.get('/fotos/9999')
    assert resposta.status_code == 404


def test_status_retorna_ok(cliente):
    resposta = cliente.get('/status')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['status'] == 'ok'