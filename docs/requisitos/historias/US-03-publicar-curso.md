# US-03 — Publicar curso

**Persona:** Coordenador
**Rastreabilidade:** Processo 01 (Publicar curso no Sympla — abrir inscrições)

## História

Como **coordenador**, quero **publicar um curso em rascunho**, para **que ele fique visível e os alunos possam se inscrever no período de inscrição**.

## Critérios de aceitação

1. **Dado** um curso em rascunho com todos os campos obrigatórios válidos, **quando** clico em "publicar", **então** o status muda para **publicado** e o curso passa a aparecer para os alunos.
2. **Dado** um curso publicado, **quando** a data atual está fora do período de inscrição, **então** o curso aparece, mas não aceita novas inscrições.
3. **Dado** um curso publicado, **quando** edito seus dados, **então** as alterações valem imediatamente. *(a confirmar: quais campos podem mudar depois que já existem inscritos, por exemplo valor e vagas)*
4. **Dado** um curso publicado sem nenhum módulo, **quando** publico, **então** o sistema permite a publicação, já que os módulos podem ser cadastrados depois (US-02). *(a confirmar)*

## Fora do escopo

- Despublicar ou cancelar um curso.
- Divulgação do curso em outros canais.
