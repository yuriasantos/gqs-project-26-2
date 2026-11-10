import pytest

from usuario import Usuario
from repositorio_usuarios import RepositorioUsuariosEmMemoria
from servico_cadastro import ServicoCadastro


def test_us04_c2_recusa_email_ja_cadastrado():
    # Preparar: já existe um usuário com esse e-mail
    repositorio = RepositorioUsuariosEmMemoria()
    existente = Usuario(
        nome="Michele Carvalho",
        email="michele@exemplo.com",
        senha_hash="hash-existente",
    )
    repositorio.salvar(existente)
    servico = ServicoCadastro(repositorio)

    # Executar e verificar: recusar o segundo cadastro
    with pytest.raises(ValueError, match="E-mail já cadastrado"):
        servico.cadastrar(
            nome="Outra pessoa",
            email="michele@exemplo.com",
            senha_hash="outro-hash",
        )

    # O cadastro original deve continuar preservado
    assert repositorio.buscar_por_email(existente.email) is existente
def test_us04_c1_servico_cadastra_usuario_com_email_disponivel():
    # Preparar
    repositorio = RepositorioUsuariosEmMemoria()
    servico = ServicoCadastro(repositorio)

    # Executar
    usuario = servico.cadastrar(
        nome="Michele Carvalho",
        email="michele@exemplo.com",
        senha_hash="hash-ficticio",
    )

    # Verificar
    assert usuario.nome == "Michele Carvalho"
    assert usuario.email == "michele@exemplo.com"
    assert repositorio.buscar_por_email(usuario.email) is usuario   