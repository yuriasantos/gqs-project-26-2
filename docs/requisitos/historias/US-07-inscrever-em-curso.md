# US-07 — Inscrever-se em um curso

**Persona:** Aluno
**Rastreabilidade:** Processo 02 (início: nova inscrição) · Decisão D-01 · RN-01.1

## História

Como **aluno**, quero **me inscrever em um curso publicado e receber as instruções de pagamento**, para **garantir minha participação**.

## Critérios de aceitação

1. **Dado** que estou logado e o curso está no período de inscrição e tem vagas, **quando** me inscrevo, **então** minha inscrição é criada com status **aguardando pagamento**.
2. **Dado** que acabei de me inscrever, **então** vejo na tela e recebo por e-mail o valor da matrícula e as instruções de pagamento. *(a confirmar: uma chave Pix única do cliente, cadastrada no sistema)*
3. **Dado** que já estou inscrito no curso, **quando** tento me inscrever de novo, **então** o sistema não cria uma segunda inscrição.
4. **Dado** um curso sem vagas ou fora do período de inscrição, **então** não consigo me inscrever.
5. **Regra de vagas:** *(a confirmar)* a vaga é ocupada **na inscrição** ou **só quando o pagamento é confirmado**?

## Fora do escopo

- Pagamento dentro do sistema (D-01).
- Cancelar a inscrição.
