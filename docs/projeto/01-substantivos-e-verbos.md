# Passo 1 — Sublinhar as histórias

[← Projeto da v1](README.md) · próximo: [Passo 2 — Filtrar os candidatos](02-classes.md)

## A técnica

> "nouns depict objects; verbs depict methods; and adjectives depict attributes"
> — SWEBOK v4, §5.4, p. 3-11

Lemos cada história e cada critério de aceitação e anotamos:

| No texto | Candidato a |
|---|---|
| **substantivo** (coisa) | classe ou atributo |
| *verbo* (ação) | método |
| adjetivo ou estado | atributo (ou valor de um atributo) |

Duas ressalvas do Sommerville (2016, slides do cap. 7):

- é **uma** de quatro técnicas para identificar classes; as outras partem das coisas tangíveis do domínio, do comportamento e dos cenários (sl. 17);
- "There is no 'magic formula' for object identification" e o processo é **iterativo**: "You are unlikely to get it right first time" (sl. 16).

Por isso este passo produz **candidatos**, não classes. O filtro é o [passo 2](02-classes.md).

## História por história

| US | Substantivos | Verbos | Adjetivos / estados |
|---|---|---|---|
| [US-01](../requisitos/historias/US-01-cadastrar-curso.md) Cadastrar curso | coordenador, curso, nome, descrição, cronograma, modalidade, carga horária, datas do curso, período de inscrição, número de vagas, valor da matrícula, campo | *cadastrar*, *preencher*, *salvar*, *editar*, *recusar* | **rascunho**, gravado, síncrono, obrigatório, limite do Meet |
| [US-02](../requisitos/historias/US-02-gerenciar-modulos.md) Gerenciar módulos | curso, módulo, título, data, link de acesso | *cadastrar*, *adicionar*, *editar*, *remover*, *recusar* | síncrono, gravado, inválido, publicado |
| [US-03](../requisitos/historias/US-03-publicar-curso.md) Publicar curso | curso, período de inscrição, módulo | *publicar*, *editar*, *aceitar (inscrições)* | **rascunho**, **publicado**, visível |
| [US-04](../requisitos/historias/US-04-criar-conta-aluno.md) Criar conta | aluno, conta, nome completo, e-mail, senha, área | *criar*, *cadastrar*, *entrar* | único, inválido |
| [US-05](../requisitos/historias/US-05-fazer-login.md) Fazer login | aluno, coordenador, e-mail, senha, sessão, perfil, área do aluno, painel | *entrar*, *sair*, *recusar* | correto, incorreto |
| [US-06](../requisitos/historias/US-06-ver-cursos-publicados.md) Ver cursos publicados | aluno, curso, lista, detalhes, módulo, link | *ver*, *escolher*, *inscrever-se* | publicado, rascunho, **inscrições encerradas**, **esgotado** |
| [US-07](../requisitos/historias/US-07-inscrever-em-curso.md) Inscrever-se | aluno, curso, inscrição, vaga, período de inscrição, valor da matrícula, instruções de pagamento, e-mail, chave Pix | *inscrever-se*, *receber*, *pagar* | publicado, **aguardando pagamento**, duplicada |
| [US-08](../requisitos/historias/US-08-confirmar-pagamento.md) Confirmar pagamento | coordenador, curso, inscrito, nome, e-mail, data da inscrição, status, pagamento, acesso, link, módulo, e-mail de acesso | *ver*, *confirmar (o pagamento)*, *liberar (o acesso)*, *enviar*, *registrar* | **aguardando pagamento**, **pagamento confirmado**, enviado (e quando) |
| [US-09](../requisitos/historias/US-09-ver-meus-cursos.md) Ver meus cursos | aluno, área, "Meus cursos", curso, inscrição, status, módulo, link, data | *ver*, *abrir*, *assistir* | **pagamento confirmado**, **aguardando pagamento**, atualizado |

Estados em **negrito** são valores que um mesmo atributo assume ao longo do tempo. Eles reaparecem no [passo 3](03-responsabilidades.md) como diagramas de estado.

## Consolidado: os candidatos

### Substantivos (agrupados pelo que parecem ser)

| Grupo | Candidatos | Aparece em |
|---|---|---|
| Coisas centrais | curso · módulo · inscrição / inscrito / matrícula | US-01 a 03, 06 a 09 |
| Pessoas | aluno · coordenador · conta · perfil | US-01, 04, 05, 07 a 09 |
| Dados de curso | nome · descrição · cronograma · modalidade · carga horária · datas do curso · período de inscrição · número de vagas · valor da matrícula · status | US-01, 03, 06 |
| Dados de módulo | título · data · link de acesso | US-02, 09 |
| Dados de pessoa | nome completo · e-mail · senha | US-04, 05 |
| Dados de inscrição | data da inscrição · status · e-mail de acesso enviado (e quando) | US-07, 08 |
| Dinheiro | pagamento · valor da matrícula · instruções de pagamento · chave Pix | US-01, 07, 08 |
| Comunicação | e-mail de acesso · e-mail com instruções de pagamento | US-07, 08 |
| Telas e sessão | área do aluno · "Meus cursos" · painel · lista · detalhes · sessão · campo | US-04 a 06, 09 |
| Externos | Google Meet · YouTube | US-01, 02, 09 |

### Verbos (com o substantivo que sofre a ação)

| Verbo | Sobre o quê | US |
|---|---|---|
| cadastrar / editar | curso | US-01 |
| adicionar / editar / remover | módulo (de um curso) | US-02 |
| publicar | curso | US-03 |
| criar | conta | US-04 |
| entrar / sair | sessão | US-05 |
| ver / listar | cursos publicados, inscritos, meus cursos | US-06, 08, 09 |
| inscrever-se | curso | US-07 |
| confirmar | pagamento (de uma inscrição) | US-08 |
| liberar | acesso (de uma inscrição) | US-08 |
| enviar / registrar | e-mail de acesso | US-07, 08 |
| recusar | qualquer operação que fere uma regra | US-01 a 05, 07 |

Repare: *recusar* aparece em quase toda história. Ele não vira um método. É o que cada método faz quando uma regra é violada (lança um erro). O [passo 3](03-responsabilidades.md) diz qual regra é de quem.

## Para fazer em sala

Escolha **uma** história que não seja a US-07 nem a US-08. Sublinhe os substantivos, circule os verbos e marque os estados. Compare com a tabela: o que você achou que não está aqui? O que está aqui e você não achou?
