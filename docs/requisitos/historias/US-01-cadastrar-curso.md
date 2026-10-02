# US-01 — Cadastrar curso

**Persona:** Coordenador
**Rastreabilidade:** Processo 01 (Elaborar documento de planejamento; Lançar informações no Sympla) · RN-01.1, RN-01.2

## História

Como **coordenador**, quero **cadastrar um curso com suas informações**, para **prepará-lo para publicação e inscrição dos alunos**.

## Campos

| Campo | Obrigatório | Observação |
|---|---|---|
| Nome | Sim | |
| Descrição / conteúdo | Sim | Texto livre |
| Cronograma | Não | Texto livre na v1 |
| Modalidade | Sim | `gravado` ou `síncrono` |
| Carga horária | Sim | Em horas |
| Datas do curso | Sim | Início e fim |
| Período de inscrição | Sim | Início e fim |
| Número de vagas | Sim | |
| Valor da matrícula | Sim | Valor fixo (RN-01.1) |

## Critérios de aceitação

1. **Dado** que estou logado como coordenador, **quando** preencho todos os campos obrigatórios e salvo, **então** o curso é criado com status **rascunho** e não aparece para os alunos.
2. **Dado** que deixei um campo obrigatório vazio, **quando** tento salvar, **então** o sistema não salva e indica o campo pendente.
3. **Dado** um período de inscrição que termina depois do fim do curso, ou uma data final anterior à inicial, **quando** tento salvar, **então** o sistema recusa e explica o erro.
4. **Dado** um curso em rascunho, **quando** edito qualquer campo e salvo, **então** as alterações ficam registradas.
5. **Dado** um curso **síncrono**, **quando** informo um número de vagas acima do limite de participantes do Google Meet, **então** o sistema recusa (RN-01.2). *(a confirmar: o limite do plano e se ele é configurável no sistema)*

## Fora do escopo

- Módulos e links de acesso → [US-02](./US-02-gerenciar-modulos.md)
- Publicação → [US-03](./US-03-publicar-curso.md)
