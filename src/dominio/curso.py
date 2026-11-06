"""Curso — implementação mínima exigida pela US-08.

A inscrição lê os módulos do curso na hora (US-09 c4), então por ora
o curso é o contêiner de `modulos`. Campos, validações e métodos de
criação/publicação chegam com US-01 a US-03.
"""

from dataclasses import dataclass, field

from dominio.modulo import Modulo


@dataclass
class Curso:
    modulos: list[Modulo] = field(default_factory=list)
