import re


class Usuario:
    def __init__(self, nome, email, senha_hash):
        if not nome.strip():
            raise ValueError("Nome obrigatório")

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            raise ValueError("E-mail em formato inválido.")

        if not senha_hash.strip():
            raise ValueError("Hash da senha obrigatório")

        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash