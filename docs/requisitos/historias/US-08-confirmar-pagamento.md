# US-08 — Ver inscritos e confirmar pagamento

**Persona:** Coordenador
**Rastreabilidade:** Processo 02 (Exportar planilha; Comparar com Gmail; Enviar e-mail em CCO) · Decisões D-01, D-03, D-04 · resolve RN-02.4 e RN-02.5

## História

Como **coordenador**, quero **ver os inscritos de um curso e confirmar o pagamento de cada um**, para **liberar o acesso sem precisar controlar quem já recebeu os links**.

## Critérios de aceitação

1. **Dado** um curso, **quando** abro seus inscritos, **então** vejo nome, e-mail, data da inscrição e status (**aguardando pagamento** / **pagamento confirmado**).
2. **Dado** um inscrito aguardando pagamento, **quando** confirmo o pagamento, **então** o status muda para **pagamento confirmado**, o acesso aos links é liberado na área do aluno e o sistema envia ao aluno um e-mail com os links dos módulos (D-03, D-04).
3. **Dado** um inscrito com pagamento já confirmado, **então** não é possível confirmar de novo, e o e-mail de acesso não é reenviado automaticamente.
4. **Dado** um inscrito, **então** o sistema registra se o e-mail de acesso foi enviado e quando, substituindo a conferência manual na caixa "Enviados" do Gmail (RN-02.5).
5. *(a confirmar: o coordenador pode desfazer uma confirmação feita por engano?)*

## Fora do escopo

- Reenviar o e-mail de acesso: na v1, assume-se que o e-mail enviado foi recebido.
