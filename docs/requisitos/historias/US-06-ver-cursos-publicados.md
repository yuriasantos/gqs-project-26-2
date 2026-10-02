# US-06 — Ver cursos publicados

**Persona:** Aluno
**Rastreabilidade:** Processo 01 (fim: curso publicado, inscrições abertas)

## História

Como **aluno**, quero **ver os cursos publicados e os detalhes de cada um**, para **escolher em qual me inscrever**.

## Critérios de aceitação

1. **Dado** que existem cursos publicados, **quando** acesso a lista de cursos, **então** vejo nome, modalidade, datas, carga horária e valor de cada um.
2. **Dado** um curso da lista, **quando** abro seus detalhes, **então** vejo também a descrição, o cronograma, o período de inscrição e a lista de módulos, **sem os links**.
3. **Dado** um curso em rascunho, **então** ele nunca aparece para o aluno.
4. **Dado** um curso fora do período de inscrição ou sem vagas, **então** ele aparece indicado como "inscrições encerradas" ou "esgotado", sem a opção de se inscrever.
5. *(a confirmar: a lista de cursos pode ser vista sem login?)*
