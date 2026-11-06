"""Módulo — implementação mínima exigida pela US-08/US-09.

O aluno vê os módulos com seus links após a confirmação (US-09 c2);
no síncrono, também a data de cada módulo. A validação do link como
URL (US-02 c4) chega com a US-02.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Modulo:
    titulo: str
    link: str
    data: date | None = None
