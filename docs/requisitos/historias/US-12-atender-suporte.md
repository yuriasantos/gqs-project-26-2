# US-12 — Ver e atender solicitações de suporte

**Persona:** Coordenador
**Rastreabilidade:** Funcionalidade nova · complementa a US-11
**Versão:** depois da v1 (fora do escopo atual)

## História

Como **coordenador**, quero **ver as solicitações de suporte dos alunos em um painel e respondê-las**, para **resolver os problemas sem depender de e-mails soltos**.

## Critérios de aceitação

1. **Dado** que estou logado como coordenador, **quando** abro o painel de suporte, **então** vejo as solicitações com aluno, curso (se houver), assunto, data e status, com as mais antigas em aberto primeiro.
2. **Dado** o painel, **quando** filtro por status, **então** vejo só as solicitações **abertas**, **em atendimento** ou **resolvidas**.
3. **Dado** uma solicitação, **quando** a abro, **então** vejo a descrição completa e posso escrever uma resposta.
4. **Dado** uma solicitação, **quando** respondo ou mudo o status, **então** a alteração aparece para o aluno em "Meu suporte" (US-11).
5. **Dado** que existe uma solicitação aberta, **então** o painel destaca a quantidade de solicitações abertas.
