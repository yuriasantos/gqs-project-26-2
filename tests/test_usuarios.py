"""Verificações do armazenamento das credenciais."""

from aplicacao.autenticacao import Perfil, RepositorioUsuarios


def test_senhas_iguais_tem_hashes_distintos_e_persistem(tmp_path):
    caminho = tmp_path / "usuarios.sqlite3"
    repositorio = RepositorioUsuarios(caminho)
    repositorio.adicionar("Ana", "ana@exemplo.com", "Senha-forte-123", Perfil.ALUNO)
    repositorio.adicionar("Bia", "bia@exemplo.com", "Senha-forte-123", Perfil.COORDENADOR)
    reaberto = RepositorioUsuarios(caminho)
    ana = reaberto.autenticar("ana@exemplo.com", "Senha-forte-123")
    bia = reaberto.autenticar("bia@exemplo.com", "Senha-forte-123")
    assert ana.senha_hash != bia.senha_hash
    assert "Senha-forte-123" not in ana.senha_hash
    assert b"Senha-forte-123" not in caminho.read_bytes()
    assert reaberto.autenticar("ana@exemplo.com", "errada") is None
    assert ana.perfil == Perfil.ALUNO
    assert bia.perfil == Perfil.COORDENADOR
