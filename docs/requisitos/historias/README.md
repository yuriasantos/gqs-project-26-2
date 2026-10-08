# Histórias de usuário — v1

## Visão da v1

Primeira versão **muito simples** de um sistema próprio para gestão de cursos online.

| Ferramenta atual | Na v1 |
|---|---|
| Sympla (publicação e inscrições) | **Substituído** pelo sistema |
| Gmail (envio dos links em CCO) | **Substituído**: o sistema gerencia os e-mails |
| Planilha de inscritos | **Substituída**: os inscritos ficam registrados no sistema |
| Google Meet (síncrono) | Mantido |
| YouTube (gravado, vídeo não listado) | Mantido |

## Decisões de escopo

- **D-01 — Pagamento fora do sistema:** a v1 não integra meio de pagamento. O aluno paga por fora (ex.: Pix) e o coordenador confirma o pagamento no sistema.
- **D-02 — Conta do aluno:** o aluno cria uma conta (login e senha) e tem uma área própria com os seus cursos.
- **D-03 — Acesso liberado após o pagamento:** os links de acesso (Meet/YouTube) só ficam disponíveis para o aluno depois que o coordenador confirma o pagamento.
- **D-04 — Links na área do aluno e no e-mail:** com o acesso liberado, os links aparecem na área do aluno e também são enviados por e-mail pelo sistema.

## Personas

| Persona | Descrição |
|---|---|
| **Coordenador** | Cuida do curso: cadastra, publica e acompanha os inscritos |
| **Aluno** | Participa do curso: se inscreve e recebe o acesso |

## Backlog

| ID | História | Persona | Processo | Status |
|---|---|---|---|---|
| US-01 | [Cadastrar curso](./US-01-cadastrar-curso.md) | Coordenador | 01 | Rascunho |
| US-02 | [Gerenciar módulos do curso](./US-02-gerenciar-modulos.md) | Coordenador | 01 | Rascunho |
| US-03 | [Publicar curso](./US-03-publicar-curso.md) | Coordenador | 01 | Rascunho |
| US-04 | [Criar conta de aluno](./US-04-criar-conta-aluno.md) | Aluno | — | Rascunho |
| US-05 | [Fazer login](./US-05-fazer-login.md) | Aluno, Coordenador | — | Rascunho |
| US-06 | [Ver cursos publicados](./US-06-ver-cursos-publicados.md) | Aluno | 01 | Rascunho |
| US-07 | [Inscrever-se em um curso](./US-07-inscrever-em-curso.md) | Aluno | 02 | Rascunho |
| US-08 | [Ver inscritos e confirmar pagamento](./US-08-confirmar-pagamento.md) | Coordenador | 02 | Rascunho |
| US-09 | [Ver meus cursos e links de acesso](./US-09-ver-meus-cursos.md) | Aluno | 02 | Rascunho |

## Depois da v1

Histórias fora do escopo da v1, mantidas para versões futuras.

| ID | História | Persona | Processo | Status |
|---|---|---|---|---|
| US-10 | [Comentar nos vídeos/módulos](./US-10-comentar-modulo.md) | Aluno | Novo | Rascunho |
| US-11 | [Solicitar suporte](./US-11-solicitar-suporte.md) | Aluno | Novo | Rascunho |
| US-12 | [Ver e atender solicitações de suporte](./US-12-atender-suporte.md) | Coordenador | Novo | Rascunho |

## Convenções

- Um arquivo por história: `US-NN-<slug>.md`.
- Formato: *Como \<persona\>, quero \<ação\>, para \<benefício\>* + critérios de aceitação (Dado/Quando/Então).
- Rastreabilidade: cada história indica o processo AS-IS e as regras de negócio (`RN-NN.n`) relacionadas.
- Pontos não confirmados ficam marcados com *(a confirmar)*.
