# US-05 — Fazer login

**Persona:** Aluno, Coordenador
**Rastreabilidade:** Decisão D-02

## História

Como **aluno ou coordenador**, quero **entrar no sistema com e-mail e senha**, para **acessar as funcionalidades do meu perfil**.

## Critérios de aceitação

1. **Dado** um e-mail e uma senha corretos, **quando** faço login, **então** entro na minha área: a do aluno ou o painel do coordenador, conforme o perfil.
2. **Dado** um e-mail ou uma senha incorretos, **quando** tento entrar, **então** o sistema recusa com uma mensagem genérica, sem dizer qual dos dois está errado.
3. **Dado** que estou logado, **quando** clico em "sair", **então** a sessão termina.

## Fora do escopo

- Recuperação de senha.
