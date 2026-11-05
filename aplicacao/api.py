"""Rotas de autenticação e áreas protegidas da US-05."""

import secrets

from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, ConfigDict

from aplicacao.autenticacao import Perfil, RepositorioUsuarios


class Credenciais(BaseModel):
    model_config = ConfigDict(hide_input_in_errors=True)
    email: str
    senha: str


def criar_aplicacao(usuarios: RepositorioUsuarios) -> FastAPI:
    app = FastAPI(title="Cursos online — US-05")
    sessoes = {}

    @app.post("/login")
    def entrar(credenciais: Credenciais, resposta: Response):
        usuario = usuarios.autenticar(credenciais.email, credenciais.senha)
        if usuario is None:
            raise HTTPException(401, "E-mail ou senha incorretos.")
        token = secrets.token_urlsafe(32)
        sessoes[token] = usuario
        resposta.set_cookie("sessao", token, httponly=True, secure=True, samesite="strict")
        destino = "/area-aluno" if usuario.perfil == Perfil.ALUNO else "/painel-coordenador"
        return {"perfil": usuario.perfil, "destino": destino}

    def acessar_area(requisicao: Request, perfil: Perfil):
        usuario = sessoes.get(requisicao.cookies.get("sessao"))
        if usuario is None:
            raise HTTPException(401, "Sessão inválida ou encerrada.")
        if usuario.perfil != perfil:
            raise HTTPException(403, "Acesso não permitido para este perfil.")
        return {"nome": usuario.nome, "email": usuario.email, "perfil": usuario.perfil}

    @app.get("/area-aluno")
    def area_aluno(requisicao: Request):
        return acessar_area(requisicao, Perfil.ALUNO)

    @app.get("/painel-coordenador")
    def painel_coordenador(requisicao: Request):
        return acessar_area(requisicao, Perfil.COORDENADOR)

    return app
