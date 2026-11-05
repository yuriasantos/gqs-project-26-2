"""Usuários persistidos e verificação de credenciais, sem dependência web."""

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import hmac
import secrets
import sqlite3


class Perfil(StrEnum):
    ALUNO = "aluno"
    COORDENADOR = "coordenador"


@dataclass(frozen=True)
class Usuario:
    nome: str
    email: str
    senha_hash: str
    perfil: Perfil


def gerar_hash(senha: str, sal: str | None = None) -> str:
    sal = sal or secrets.token_hex(16)
    resumo = hashlib.pbkdf2_hmac("sha256", senha.encode(), bytes.fromhex(sal), 600_000)
    return f"{sal}:{resumo.hex()}"


class RepositorioUsuarios:
    def __init__(self, caminho):
        self.caminho = caminho
        with sqlite3.connect(self.caminho) as banco:
            banco.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                nome TEXT NOT NULL, email TEXT PRIMARY KEY,
                senha_hash TEXT NOT NULL, perfil TEXT NOT NULL)""")

    def adicionar(self, nome: str, email: str, senha: str, perfil: Perfil):
        with sqlite3.connect(self.caminho) as banco:
            banco.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)",
                          (nome, email.strip().lower(), gerar_hash(senha), perfil.value))

    def autenticar(self, email: str, senha: str) -> Usuario | None:
        with sqlite3.connect(self.caminho) as banco:
            linha = banco.execute("SELECT nome, email, senha_hash, perfil FROM usuarios WHERE email = ?",
                                  (email.strip().lower(),)).fetchone()
        if linha is None:
            return None
        usuario = Usuario(*linha[:3], Perfil(linha[3]))
        sal = usuario.senha_hash.split(":")[0]
        if hmac.compare_digest(gerar_hash(senha, sal), usuario.senha_hash):
            return usuario
        return None
