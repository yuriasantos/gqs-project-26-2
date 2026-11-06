"""Domínio da v1 — Python puro, sem dependência de FastAPI.

Implementação bottom-up: cada bloco manipula o próprio estado.
Rastreabilidade: docs/projeto/03-responsabilidades.md
"""

from dominio.curso import Curso
from dominio.inscricao import Inscricao, PagamentoJaConfirmado, StatusInscricao
from dominio.modulo import Modulo
from dominio.usuario import Usuario

__all__ = [
    "Curso",
    "Inscricao",
    "Modulo",
    "PagamentoJaConfirmado",
    "StatusInscricao",
    "Usuario",
]
