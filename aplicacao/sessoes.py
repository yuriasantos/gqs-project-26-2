"""Sessões opacas mantidas no servidor, com revogação e validade fixa."""

from collections.abc import Callable
from dataclasses import dataclass
import secrets
from time import monotonic

from aplicacao.autenticacao import Usuario


@dataclass(frozen=True)
class Sessao:
    usuario: Usuario
    expira_em: float


class GerenciadorSessoes:
    DURACAO = 3600

    def __init__(self, relogio: Callable[[], float] = monotonic):
        self._relogio = relogio
        self._sessoes: dict[str, Sessao] = {}

    def criar(self, usuario: Usuario) -> str:
        agora = self._relogio()
        self._sessoes = {token: sessao for token, sessao in self._sessoes.items()
                         if sessao.expira_em > agora}
        token = secrets.token_urlsafe(32)
        self._sessoes[token] = Sessao(usuario, agora + self.DURACAO)
        return token

    def obter_usuario(self, token: str | None) -> Usuario | None:
        sessao = self._sessoes.get(token)
        if sessao is None:
            return None
        if self._relogio() >= sessao.expira_em:
            self.encerrar(token)
            return None
        return sessao.usuario

    def encerrar(self, token: str | None) -> None:
        self._sessoes.pop(token, None)
