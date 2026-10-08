# Projeto da v1 — das histórias às classes

Como as histórias de usuário da v1 (US-01 a US-09, em [`../requisitos/historias/`](../requisitos/historias/README.md)) viram um projeto orientado a objetos, construído **bottom-up** e implementado em **FastAPI**.

Requisito diz **o quê**; projeto diz **como** (Vasconcelos et al., 2006, p. 63).

## Os passos

| # | Passo | Pergunta que responde | Saída | Status |
|---|---|---|---|---|
| 1 | [Sublinhar as histórias](01-substantivos-e-verbos.md) | Que coisas, ações e estados aparecem no texto? | Lista de candidatos | Rascunho |
| 2 | [Filtrar os candidatos](02-classes.md) | Quais candidatos viram classe, atributo ou nada? | Diagrama de classes (estrutura) | Rascunho |
| 3 | [Dar cada regra a um dono](03-responsabilidades.md) | Que classe cuida de cada critério de aceitação? | Métodos, diagramas de estado, matriz história → método → teste | Rascunho |
| 4 | Desenhar a conversa entre os objetos | Como as classes colaboram numa história? | Diagramas de sequência (US-07, US-08) | A fazer |
| 5 | Montar as camadas, de baixo para cima | Em que ordem construir, e onde entra o FastAPI? | Ordem de construção, mapa história → endpoint | A fazer |

## Duas ideias que não se confundem

- **A técnica gramatical (passo 1) diz *quais* blocos existem.** É uma das técnicas de identificação de classes (Sommerville, 2016, slides do cap. 7, sl. 17); serviria também a um projeto feito top-down.
- **O bottom-up diz *em que ordem* construí-los.** Primeiro os blocos (`Periodo`, `Curso`, `Inscricao`…), cada um com seus testes; por último o que os compõe (serviços e rotas). "O sistema é visto como uma coleção de 'building-blocks' […] cada objeto manipula seu próprio estado" (Vasconcelos et al., 2006, p. 64). É o que os passos 3 e 5 tornam concreto.

## Convenções

- Diagramas em **Mermaid** (o GitHub desenha sozinho), como nas fichas de processo.
- Critérios de aceitação citados como `US-NN cN` (ex.: `US-07 c3` = história US-07, critério 3).
- Pontos não confirmados pelo cliente: *(a confirmar)*, como no resto do repositório.
- O domínio é **Python puro**: as classes destes documentos não dependem do FastAPI.

## Fontes

- IEEE Computer Society. *SWEBOK Guide* v4.0a, 2024. Cap. 3 *Software Design*, §5.4 *Object-Oriented Design*, p. 3-11.
- Sommerville, I. *Software Engineering*, 10. ed., 2016. Slides oficiais do cap. 7 *Design and Implementation*, sl. 16–17.
- Vasconcelos, A. M. L. et al. *Introdução à Engenharia de Software e à Qualidade de Software*. UFLA/FAEPE, 2006. §5.2, pp. 63–64.
