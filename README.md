# US-04 — Criar conta de aluno

Implementação acadêmica das classes e dos testes unitários
relacionados ao cadastro de aluno.

Autora: Michele Carvalho.

## Tecnologias

- Python — execução validada com a versão 3.14.6.
- pytest — versão definida em requirements-dev.txt.

## Estrutura

- usuario.py: representa o usuário e valida nome, e-mail e hash obrigatório.
- repositorio_usuarios.py: armazena e consulta usuários em memória.
- servico_cadastro.py: coordena o cadastro e recusa e-mail duplicado.
- test_usuario.py: testes das validações do usuário.
- test_repositorio_usuarios.py: testes de armazenamento e consulta.
- test_servico_cadastro.py: testes do serviço de cadastro.

## Executar no Windows

Na pasta do projeto, execute:

```cmd
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -v
```

## Cenários verificados

1. Recusar e-mail em formato inválido.
2. Criar usuário com dados válidos.
3. Recusar nome vazio.
4. Recusar nome contendo apenas espaços.
5. Recusar hash de senha vazio.
6. Salvar e consultar usuário pelo e-mail.
7. Retornar None para e-mail não cadastrado.
8. Recusar e-mail duplicado e preservar o cadastro original.
9. Cadastrar e armazenar usuário com e-mail disponível.

Resultado observado: 9 testes passaram.

## Relação com os requisitos

- US-04, critério 1: criação do usuário e cadastro em memória.
- US-04, critério 2: recusa de e-mail duplicado com mensagem
  sugerindo login.
- US-04, critério 3: validação básica do formato do e-mail.
- Campos obrigatórios: validações de nome e hash de senha.

## Limites da implementação

Esta entrega cobre classes e testes unitários. Não implementa
interface, API, banco de dados, login ou sessão.

O serviço recebe um hash pronto. Não realiza a transformação
da senha original em hash nem verifica sua segurança.

A possibilidade de entrar no sistema após o cadastro, prevista
no critério 1, ainda depende da implementação de autenticação.

Os dados são temporários e ficam em memória. A validação do
e-mail verifica um formato básico, sem confirmar sua existência.

A regra mínima de senha permanece a confirmar na documentação.