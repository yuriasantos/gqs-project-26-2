# US-02 — Gerenciar módulos do curso

**Persona:** Coordenador
**Rastreabilidade:** Processo 01 (Criar reunião no Meet para cada dia/módulo) · RN-01.3, RN-02.2, RN-02.3

## História

Como **coordenador**, quero **cadastrar os módulos de um curso com seus links de acesso, inclusive depois de criar o curso**, para **definir o que o aluno vai acessar**.

## Campos do módulo

| Campo | Obrigatório | Observação |
|---|---|---|
| Título | Sim | |
| Data | Só no síncrono | Um módulo por dia (RN-01.3) |
| Link de acesso | Sim | Google Meet (síncrono) ou vídeo não listado do YouTube (gravado) |

## Critérios de aceitação

1. **Dado** um curso já cadastrado, **quando** adiciono um módulo com os campos obrigatórios, **então** ele passa a fazer parte do curso.
2. **Dado** um curso com módulos, **quando** edito ou removo um módulo, **então** a alteração fica registrada.
3. **Dado** um curso **síncrono**, **quando** cadastro um módulo sem data ou com data fora do período do curso, **então** o sistema recusa.
4. **Dado** que informo um link inválido (que não é uma URL), **quando** salvo, **então** o sistema recusa.
5. **Dado** um curso já publicado, **quando** adiciono ou altero módulos, **então** a alteração é permitida. *(a confirmar: alunos com acesso já liberado devem ser avisados por e-mail?)*

## Fora do escopo

- Criar a reunião no Meet ou subir o vídeo no YouTube: continua sendo feito fora do sistema; aqui só se registra o link.
