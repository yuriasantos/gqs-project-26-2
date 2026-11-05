"""Prepara usuários existentes para demonstrar o login; não expõe cadastro público."""

import argparse
from getpass import getpass
import os
import sqlite3

from aplicacao.autenticacao import Perfil, RepositorioUsuarios


def main(argumentos=None):
    parser = argparse.ArgumentParser(description="Preparar um usuário para demonstrar a US-05.")
    parser.add_argument("--nome", required=True)
    parser.add_argument("--email", required=True)
    parser.add_argument("--perfil", choices=[perfil.value for perfil in Perfil], required=True)
    parser.add_argument("--banco", default=os.environ.get("BANCO_USUARIOS", "usuarios.sqlite3"))
    dados = parser.parse_args(argumentos)
    senha = getpass("Senha (não será exibida): ")
    if not senha or not dados.nome.strip() or not dados.email.strip():
        parser.error("Nome, e-mail e senha precisam estar preenchidos.")
    try:
        RepositorioUsuarios(dados.banco).adicionar(dados.nome, dados.email, senha, Perfil(dados.perfil))
    except sqlite3.IntegrityError:
        parser.error("Já existe um usuário com esse e-mail.")
    print("Usuário preparado com sucesso.")


if __name__ == "__main__":
    main()
