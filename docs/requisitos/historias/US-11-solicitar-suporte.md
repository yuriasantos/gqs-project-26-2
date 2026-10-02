# US-11 — Solicitar suporte

**Persona:** Aluno
**Rastreabilidade:** Funcionalidade nova · cobre as exceções do Processo 02 (ex.: "aluno diz que não recebeu", "e-mail cadastrado errado")

## História

Como **aluno**, quero **abrir uma solicitação de suporte**, para **resolver problemas de acesso, pagamento ou dúvidas sobre o curso**.

## Critérios de aceitação

1. **Dado** que estou logado, **quando** abro uma solicitação informando o assunto e a descrição, **então** ela é registrada com status **aberta** e aparece no painel do coordenador (US-12).
2. **Dado** que estou abrindo uma solicitação, **então** posso indicar a qual dos meus cursos ela se refere (opcional).
3. **Dado** que abri solicitações, **quando** acesso "Meu suporte", **então** vejo cada solicitação com status e resposta.
4. **Dado** que o coordenador respondeu ou mudou o status da minha solicitação, **então** recebo um e-mail avisando. *(a confirmar)*
5. **Dado** uma solicitação sem assunto ou sem descrição, **quando** tento enviar, **então** o sistema não aceita.

## Pontos em aberto *(a confirmar)*

- O aluno pode responder de volta (conversa), ou é uma pergunta e uma resposta só?
- Precisa de categorias (acesso, pagamento, conteúdo, outro)?
