from usuario import Usuario
from repositorio_usuarios import RepositorioUsuariosEmMemoria


def test_repositorio_salva_e_busca_usuario_por_email():
    # Preparar
    repositorio = RepositorioUsuariosEmMemoria()
    usuario = Usuario(
        nome="Michele Carvalho",
        email="michele@exemplo.com",
        senha_hash="hash-ficticio",
    )

    # Executar
    repositorio.salvar(usuario)
    encontrado = repositorio.buscar_por_email("michele@exemplo.com")

    # Verificar
    assert encontrado is usuario
def test_repositorio_retorna_none_para_email_nao_cadastrado():
    repositorio = RepositorioUsuariosEmMemoria()

    encontrado = repositorio.buscar_por_email("novo@exemplo.com")

    assert encontrado is None