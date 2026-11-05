"""Testes de aceitação da US-05, exercitando a API real."""

import pytest
from fastapi.testclient import TestClient

from aplicacao.api import criar_aplicacao
from aplicacao.autenticacao import Perfil, RepositorioUsuarios


@pytest.fixture
def usuarios(tmp_path):
    repositorio = RepositorioUsuarios(tmp_path / "usuarios.sqlite3")
    repositorio.adicionar("Ana", "aluno@exemplo.com", "Senha-forte-123", Perfil.ALUNO)
    repositorio.adicionar("Bia", "coord@exemplo.com", "Outra-senha-456", Perfil.COORDENADOR)
    return repositorio


@pytest.fixture
def cliente(usuarios):
    with TestClient(criar_aplicacao(usuarios), base_url="https://testserver") as cliente:
        yield cliente


@pytest.mark.parametrize("email,senha,perfil,destino", [
    ("aluno@exemplo.com", "Senha-forte-123", "aluno", "/area-aluno"),
    ("coord@exemplo.com", "Outra-senha-456", "coordenador", "/painel-coordenador"),
])
def test_c1_login_abre_area_do_perfil(cliente, email, senha, perfil, destino):
    resposta = cliente.post("/login", json={"email": email, "senha": senha})
    assert resposta.status_code == 200
    assert resposta.json() == {"perfil": perfil, "destino": destino}
    assert cliente.cookies.get("sessao")
    area = cliente.get(destino)
    assert area.status_code == 200
    assert area.json()["email"] == email
    assert area.json()["perfil"] == perfil
    assert "senha" not in area.text


def test_c1_aluno_nao_acessa_painel_do_coordenador(cliente):
    cliente.post("/login", json={"email": "aluno@exemplo.com", "senha": "Senha-forte-123"})
    assert cliente.get("/painel-coordenador").status_code == 403


@pytest.mark.parametrize("dados", [
    {"email": "ausente@exemplo.com", "senha": "Senha-forte-123"},
    {"email": "aluno@exemplo.com", "senha": "incorreta"},
    {"email": "ausente@exemplo.com", "senha": "incorreta"},
    {"email": "", "senha": ""},
    {"email": "aluno@exemplo.com", "senha": ""},
    {"email": "aluno@exemplo.com"},
    {"senha": "Senha-forte-123"},
    {},
    {"email": "' OR 1=1 --", "senha": "qualquer"},
])
def test_c2_recusa_credenciais_com_mesma_mensagem(cliente, dados):
    resposta = cliente.post("/login", json=dados)
    assert resposta.status_code == 401
    assert resposta.json() == {"detail": "E-mail ou senha incorretos."}
    assert "sessao" not in resposta.cookies
    assert cliente.get("/area-aluno").status_code == 401
