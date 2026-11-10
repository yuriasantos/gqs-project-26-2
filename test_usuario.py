import pytest

from usuario import Usuario


def test_us04_c3_recusa_email_invalido():
    with pytest.raises(ValueError):
        Usuario(
            nome="Michele Carvalho",
            email="email-invalido",
            senha_hash="hash-ficticio",
        )


def test_us04_c1_cria_usuario_com_dados_validos():
    usuario = Usuario(
        nome="Michele Carvalho",
        email="michele@exemplo.com",
        senha_hash="hash-ficticio",
    )

    assert usuario.nome == "Michele Carvalho"
    assert usuario.email == "michele@exemplo.com"
    assert usuario.senha_hash == "hash-ficticio"


def test_us04_c1_recusa_nome_vazio():
    with pytest.raises(ValueError, match="Nome obrigatório"):
        Usuario(
            nome="",
            email="michele@exemplo.com",
            senha_hash="hash-ficticio",
        )


def test_us04_c1_recusa_nome_apenas_com_espacos():
    with pytest.raises(ValueError, match="Nome obrigatório"):
        Usuario(
            nome="   ",
            email="michele@exemplo.com",
            senha_hash="hash-ficticio",
        )


def test_us04_c1_recusa_senha_hash_vazia():
    with pytest.raises(ValueError, match="Hash da senha obrigatório"):
        Usuario(
            nome="Michele Carvalho",
            email="michele@exemplo.com",
            senha_hash="",
        )