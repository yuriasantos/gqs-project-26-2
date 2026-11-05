"""Ponto de entrada para o servidor Uvicorn."""

import os

from aplicacao.api import criar_aplicacao
from aplicacao.autenticacao import RepositorioUsuarios


def obter_aplicacao():
    usuarios = RepositorioUsuarios(os.environ.get("BANCO_USUARIOS", "usuarios.sqlite3"))
    desenvolvimento = os.environ.get("AMBIENTE") == "desenvolvimento"
    return criar_aplicacao(usuarios, cookie_seguro=not desenvolvimento)
