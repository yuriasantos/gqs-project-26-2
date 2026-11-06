"""US-04 - Criar conta de aluno.

Implementação mínima para fazer os testes passarem (fase GREEN do TDD).
"""
import hashlib
import hmac
import os
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# ------------------------------------------------------------ exceções
class CampoObrigatorioError(Exception):
    """Nome, e-mail ou senha não informados."""


class EmailInvalidoError(Exception):
    """E-mail em formato inválido."""


class EmailJaCadastradoError(Exception):
    """Já existe uma conta com esse e-mail."""


class CredenciaisInvalidasError(Exception):
    """E-mail ou senha incorretos no login."""


# ------------------------------------------------------------ entidade
class Aluno:
    def __init__(self, nome, email, senha_hash, salt):
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash  # nunca guarda a senha em texto puro
        self.salt = salt

    def senha_confere(self, senha):
        hash_informado = _gerar_hash(senha, self.salt)
        return hmac.compare_digest(hash_informado, self.senha_hash)


# ------------------------------------------------------------ serviço
class ServicoConta:
    def __init__(self):
        self._alunos = {}  # chave: e-mail em minúsculas

    def criar_conta(self, nome, email, senha):
        nome = self._limpar(nome)
        email = self._limpar(email)

        self._validar_obrigatorios(nome, email, senha)
        self._validar_formato_email(email)
        self._validar_email_unico(email)

        salt = os.urandom(16)
        aluno = Aluno(nome, email, _gerar_hash(senha, salt), salt)
        self._alunos[email.lower()] = aluno
        return aluno

    def entrar(self, email, senha):
        aluno = self._alunos.get(self._limpar(email).lower())
        if aluno is None or not aluno.senha_confere(senha):
            raise CredenciaisInvalidasError("E-mail ou senha inválidos.")
        return aluno

    def total_contas(self):
        return len(self._alunos)

    # -------------------------------------------------- auxiliares
    @staticmethod
    def _limpar(valor):
        return valor.strip() if isinstance(valor, str) else valor or ""

    @staticmethod
    def _validar_obrigatorios(nome, email, senha):
        if not nome:
            raise CampoObrigatorioError("O campo nome é obrigatório.")
        if not email:
            raise CampoObrigatorioError("O campo e-mail é obrigatório.")
        if not senha:
            raise CampoObrigatorioError("O campo senha é obrigatório.")

    @staticmethod
    def _validar_formato_email(email):
        if not EMAIL_REGEX.match(email):
            raise EmailInvalidoError("Formato de e-mail inválido.")

    def _validar_email_unico(self, email):
        if email.lower() in self._alunos:
            raise EmailJaCadastradoError(
                "E-mail já cadastrado. Faça login."
            )


def _gerar_hash(senha, salt):
    return hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, 100_000)