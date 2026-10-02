# CLAUDE.md

## Sobre o projeto

Mapeamento de processos de negócio (BPM) de um cliente que vende **cursos online**. Por enquanto não há código: o repositório contém apenas documentação de processos **AS-IS** (como são executados hoje), com o objetivo futuro de propor um **TO-BE** (processos melhorados/automatizados).

Idioma de todo o conteúdo: **português (pt-BR)**.

## Contexto do cliente (resumo)

- Cursos têm modalidade **gravado** (vídeos não listados no YouTube, 1 por módulo) ou **síncrono** (Google Meet pago, 1 reunião por dia/módulo).
- Cursos são publicados e recebem inscrições pelo **Sympla**; a matrícula tem valor fixo por curso.
- O acesso é liberado manualmente: exportam a planilha de inscritos do Sympla, comparam com a caixa "Enviados" do Gmail e enviam os links por e-mail em **CCO**.
- Dores já identificadas (insumo para o TO-BE): sem controle de quem recebeu o link (risco de duplicidade/esquecimento), sem confirmação de entrega, links do YouTube repassáveis e não revogáveis, limite de participantes do Meet.
- O ator principal ("Coordenação de cursos") ainda é **hipótese a confirmar**.

## Estrutura

```
docs/processos/
├── README.md        # índice dos processos e convenções
├── glossario.md     # vocabulário do cliente
└── as-is/
    ├── NN-nome-do-processo.bpmn  # diagrama BPMN 2.0 com DI
    └── NN-nome-do-processo.md    # ficha do processo
```

Processos mapeados: `01` Criação e publicação de curso; `02` Liberação de acesso ao curso (ambos em rascunho, com dúvidas abertas).

## Convenções

- **Cada processo = par `.bpmn` + `.md`** com o mesmo nome, numerado com 2 dígitos (`03-...`). Ao criar um novo, atualizar a tabela em `docs/processos/README.md`.
- **Ficha `.md`** segue a ordem: link para o `.bpmn` → *Ficha do processo* (Objetivo, Evento de início/fim, Atores, Sistemas, Artefatos, Frequência) → *Fluxo (prévia)* em Mermaid `flowchart LR` → *Regras de negócio* → *Observações do analista* (opcional) → *Dúvidas abertas (levar ao cliente)*.
- **Regras de negócio** numeradas `RN-<processo>.<n>` (ex.: `RN-02.3`). Não renumerar regras existentes.
- **Tarefas**: verbo no infinitivo + objeto ("Elaborar documento de planejamento").
- **Hipóteses** não confirmadas pelo cliente marcadas com *(a confirmar)* — nos `.md` e também nos nomes de lanes/anotações do BPMN.
- **Dúvidas respondidas**: riscar (`~~...~~`) e registrar a resposta com **Respondido:**, em vez de apagar. Propagar a resposta para a ficha, as regras, o Mermaid e o `.bpmn`.
- **Glossário**: todo termo novo do cliente usado nos diagramas entra em `glossario.md`, indicando o processo de origem.

## BPMN

- BPMN 2.0 **com seção DI** (`bpmndi`) — precisa abrir em <https://demo.bpmn.io> / Camunda Modeler. Ao adicionar/mover elementos, sempre criar ou ajustar as shapes/edges correspondentes.
- Padrão atual: `collaboration` com pool `Pool_Empresa` ("Empresa (cursos online)") e lane `Lane_Coordenacao`; participantes externos (ex.: `Pool_Aluno`) como pool separado ligado por `messageFlow`.
- IDs descritivos com prefixo por tipo: `Start_`, `End_`, `Task_`, `GW_`, `Flow_`, `DataObj_`/`DataObject_`, `DataStore_`, `Annot_`, `Assoc_`, `DIA_`/`DOA_`, `MF_`, `Pool_`, `Lane_`.
- Tarefas manuais feitas em sistema = `userTask`; envio de e-mail = `sendTask`. Sistemas externos (Sympla, Gmail) como `dataStoreReference`; documentos/planilhas/links como `dataObjectReference`.
- Regras de negócio e hipóteses relevantes aparecem como `textAnnotation` no diagrama.
- Manter `.bpmn` e Mermaid da ficha **consistentes** entre si.
- Validar XML após editar (ex.: `xmllint --noout arquivo.bpmn`).
