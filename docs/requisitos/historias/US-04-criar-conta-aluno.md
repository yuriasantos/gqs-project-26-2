# US-04 — Criar conta de aluno

**Persona:** Aluno
**Rastreabilidade:** Decisão D-02 · substitui o cadastro do participante no Sympla (Processo 02)

## História

Como **aluno**, quero **criar uma conta no sistema**, para **me inscrever em cursos e acompanhar meus cursos em uma área própria**.

## Campos

| Campo | Obrigatório | Observação |
|---|---|---|
| Nome completo | Sim | |
| E-mail | Sim | Único no sistema; usado para login e para os e-mails do sistema |
| Senha | Sim | *(a confirmar: regra mínima de senha)* |

## Critérios de aceitação

1. **Dado** que não tenho conta, **quando** preencho os campos obrigatórios e confirmo, **então** minha conta é criada e já posso entrar no sistema.
2. **Dado** um e-mail que já tem conta, **quando** tento me cadastrar com ele, **então** o sistema recusa e sugere fazer login.
3. **Dado** um e-mail em formato inválido, **quando** tento me cadastrar, **então** o sistema recusa.

## Fora do escopo

- Confirmação do e-mail por link. *(a confirmar se entra na v1)*
- Cadastro de coordenadores: na v1 eles são criados direto no sistema, sem tela de cadastro. *(a confirmar)*
