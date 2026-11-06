"""Inscrição — dona das regras de confirmação de pagamento e liberação de acesso.

Rastreabilidade (docs/projeto/03-responsabilidades.md):
- US-08 c2 · `confirmar_pagamento()`: status vira PAGAMENTO_CONFIRMADO
- US-08 c3 · `confirmar_pagamento()`: não confirma duas vezes
- US-08 c4 · `registrar_envio_acesso(quando)`: registra se e quando o e-mail saiu
- US-08 c2 · US-09 c2/c3 · `acesso_liberado()` e `links_liberados()`:
  links só depois da confirmação
- US-09 c4 · `links_liberados()` lê os módulos do curso na hora,
  sem guardar cópia — link atualizado sai de graça do desenho

O envio do e-mail em si (US-08 c2) não é do domínio: quem envia é um
serviço, que registra o momento aqui via `registrar_envio_acesso`.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto

from dominio.curso import Curso
from dominio.usuario import Usuario


class StatusInscricao(Enum):
    AGUARDANDO_PAGAMENTO = auto()
    PAGAMENTO_CONFIRMADO = auto()


class PagamentoJaConfirmado(Exception):
    """Lançada ao tentar confirmar uma inscrição já confirmada (US-08 c3)."""


@dataclass
class Inscricao:
    aluno: Usuario
    curso: Curso
    data: datetime
    status: StatusInscricao = field(default=StatusInscricao.AGUARDANDO_PAGAMENTO)
    acesso_enviado_em: datetime | None = field(default=None)

    def confirmar_pagamento(self) -> None:
        """US-08 c2/c3: confirma uma vez; recusa se já estiver confirmada."""
        if self.status is StatusInscricao.PAGAMENTO_CONFIRMADO:
            raise PagamentoJaConfirmado()
        self.status = StatusInscricao.PAGAMENTO_CONFIRMADO

    def registrar_envio_acesso(self, quando: datetime) -> None:
        """US-08 c4: o serviço de e-mail registra aqui quando o acesso saiu."""
        self.acesso_enviado_em = quando

    def acesso_liberado(self) -> bool:
        """US-09 c2/c3: links só aparecem após a confirmação do pagamento."""
        return self.status is StatusInscricao.PAGAMENTO_CONFIRMADO

    def links_liberados(self) -> list[str]:
        """US-09 c4: lê os módulos do curso na hora — sempre atualizado."""
        if not self.acesso_liberado():
            return []
        return [modulo.link for modulo in self.curso.modulos]
