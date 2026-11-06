"""Usuário — implementação mínima exigida pela US-08.

A US-08 c1 mostra nome e e-mail de cada inscrito; senha, perfil e as
validações de cadastro (US-04/US-05) chegam com suas histórias.
"""

from dataclasses import dataclass


@dataclass
class Usuario:
    nome: str
    email: str
