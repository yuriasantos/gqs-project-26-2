"""Verifica a preparação da aplicação e dos usuários para demonstração."""

from unittest.mock import patch

from fastapi.testclient import TestClient
import pytest

from aplicacao.autenticacao import Perfil, RepositorioUsuarios


def test_comando_prepara_usuario_com_senha_digitada(tmp_path, capsys):
    from aplicacao.criar_usuario import main

    caminho = tmp_path / "usuarios.sqlite3"
    with patch("aplicacao.criar_usuario.getpass", return_value="Senha-forte-123"):
        main(["--nome", "Ana", "--email", "ana@exemplo.com", "--perfil", "aluno", "--banco", str(caminho)])
    usuario = RepositorioUsuarios(caminho).autenticar("ana@exemplo.com", "Senha-forte-123")
    assert usuario.perfil == Perfil.ALUNO
    assert "Senha-forte-123" not in capsys.readouterr().out


@pytest.mark.parametrize("ambiente,seguro", [("producao", True), ("desenvolvimento", False)])
def test_configuracao_do_cookie_conforme_ambiente(tmp_path, monkeypatch, ambiente, seguro):
    from aplicacao.principal import obter_aplicacao

    caminho = tmp_path / "usuarios.sqlite3"
    monkeypatch.setenv("BANCO_USUARIOS", str(caminho))
    monkeypatch.setenv("AMBIENTE", ambiente)
    RepositorioUsuarios(caminho).adicionar("Ana", "ana@exemplo.com", "Senha-forte-123", Perfil.ALUNO)
    with TestClient(obter_aplicacao()) as cliente:
        resposta = cliente.post("/login", json={"email": "ana@exemplo.com", "senha": "Senha-forte-123"})
        assert resposta.status_code == 200
        assert ("; Secure" in resposta.headers["set-cookie"]) == seguro
        if not seguro:
            assert cliente.get("/area-aluno").status_code == 200
            assert cliente.post("/sair").status_code == 204
            assert cliente.get("/area-aluno").status_code == 401
