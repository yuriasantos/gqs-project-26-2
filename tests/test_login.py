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
    {"email": None, "senha": "Senha-forte-123"},
    {"email": "aluno@exemplo.com", "senha": ["Senha-forte-123"]},
])
def test_c2_recusa_credenciais_com_mesma_mensagem(cliente, dados):
    resposta = cliente.post("/login", json=dados)
    assert resposta.status_code == 401
    assert resposta.json() == {"detail": "E-mail ou senha incorretos."}
    assert "sessao" not in resposta.cookies
    assert cliente.get("/area-aluno").status_code == 401


@pytest.mark.parametrize("email,senha,destino", [
    ("aluno@exemplo.com", "Senha-forte-123", "/area-aluno"),
    ("coord@exemplo.com", "Outra-senha-456", "/painel-coordenador"),
])
def test_c3_sair_revoga_sessao_inclusive_para_token_copiado(cliente, email, senha, destino):
    cliente.post("/login", json={"email": email, "senha": senha})
    token_antigo = cliente.cookies.get("sessao")
    assert cliente.get(destino).status_code == 200
    resposta = cliente.post("/sair")
    assert resposta.status_code == 204
    assert not resposta.content
    assert cliente.cookies.get("sessao") is None
    assert cliente.get(destino).status_code == 401
    assert cliente.get(destino, headers={"Cookie": f"sessao={token_antigo}"}).status_code == 401


def test_c3_sair_sem_sessao_pode_ser_repetido(cliente):
    assert cliente.post("/sair").status_code == 204
    assert cliente.post("/sair").status_code == 204


def test_novo_login_substitui_sessao_anterior(cliente):
    dados = {"email": "aluno@exemplo.com", "senha": "Senha-forte-123"}
    cliente.post("/login", json=dados)
    token_antigo = cliente.cookies.get("sessao")
    resposta = cliente.post("/login", json=dados)
    assert cliente.cookies.get("sessao") != token_antigo
    assert cliente.get("/area-aluno").status_code == 200
    assert cliente.get("/area-aluno", headers={"Cookie": f"sessao={token_antigo}"}).status_code == 401
    cookie = resposta.headers["set-cookie"].lower()
    assert "httponly" in cookie
    assert "secure" in cookie
    assert "samesite=strict" in cookie


@pytest.mark.parametrize("destino", ["/area-aluno", "/painel-coordenador"])
def test_areas_recusam_visitante_e_token_inventado(cliente, destino):
    assert cliente.get(destino).status_code == 401
    assert cliente.get(destino, headers={"Cookie": "sessao=inventada"}).status_code == 401


def test_sessao_expira_no_servidor_mesmo_com_cookie_copiado(usuarios):
    instante = [100.0]
    app = criar_aplicacao(usuarios, relogio=lambda: instante[0])
    with TestClient(app, base_url="https://testserver") as cliente:
        resposta = cliente.post("/login", json={"email": "aluno@exemplo.com", "senha": "Senha-forte-123"})
        token = cliente.cookies.get("sessao")
        assert "Max-Age=3600" in resposta.headers["set-cookie"]
        instante[0] += 3599
        assert cliente.get("/area-aluno").status_code == 200
        instante[0] += 1
        assert cliente.get("/area-aluno", headers={"Cookie": f"sessao={token}"}).status_code == 401


def test_sair_nao_encerra_sessao_de_outro_navegador(usuarios):
    app = criar_aplicacao(usuarios)
    with TestClient(app, base_url="https://testserver") as primeiro, TestClient(app, base_url="https://testserver") as segundo:
        dados = {"email": "aluno@exemplo.com", "senha": "Senha-forte-123"}
        primeiro.post("/login", json=dados)
        segundo.post("/login", json=dados)
        primeiro.post("/sair")
        assert primeiro.get("/area-aluno").status_code == 401
        assert segundo.get("/area-aluno").status_code == 200
