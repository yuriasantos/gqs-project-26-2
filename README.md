# US-05 — Fazer login com TDD em Python

Implementação da [história escolhida](docs/requisitos/historias/US-05-fazer-login.md),
usando Python, FastAPI, SQLite e pytest. Branch: `funcionalidade/login-com-tdd`.

O nome do processo é **Test-Driven Development (TDD)**, ou desenvolvimento guiado por testes:
escrever um teste, executá-lo e observar a falha (**vermelho**); implementar o necessário
para passar (**verde**); melhorar a organização mantendo os testes passando (**refatoração**).
Os commits deste trabalho preservam essas etapas. Veja o [relatório do TDD](docs/desenvolvimento/US-05-tdd.md).

## Preparar o ambiente

Requer Python 3.11 ou superior. Validado com Python 3.14.4 no Windows.
No PowerShell, dentro da pasta deste repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pytest -q
```

## Preparar usuários para a demonstração

```powershell
.\.venv\Scripts\python -m aplicacao.criar_usuario --nome "Ana" --email "aluno@exemplo.com" --perfil aluno
.\.venv\Scripts\python -m aplicacao.criar_usuario --nome "Bia" --email "coord@exemplo.com" --perfil coordenador
```

Cada comando pede a senha sem exibi-la. Escolha uma senha para cada usuário e use-a
no login. O arquivo `usuarios.sqlite3` guarda os usuários e não é versionado.
Esse comando é apenas uma preparação administrativa: cadastro público e recuperação
de senha não fazem parte desta entrega.

## Executar e demonstrar

```powershell
$env:AMBIENTE = "desenvolvimento"
.\.venv\Scripts\python -m uvicorn aplicacao.principal:obter_aplicacao --factory --host 127.0.0.1 --port 8000
```

Abra [a documentação interativa](http://127.0.0.1:8000/docs).
Esta entrega é uma **API**, com respostas JSON para as áreas de cada perfil.
A interface interativa permite executar as operações pelo botão **Try it out**.

1. Execute `POST /login` com o e-mail e a senha de um usuário preparado:

   ```json
   {"email": "aluno@exemplo.com", "senha": "a senha escolhida ao preparar o usuário"}
   ```

2. Confira `perfil` e `destino` na resposta. O navegador recebe o cookie automaticamente.
3. Execute `GET /area-aluno` ou `GET /painel-coordenador`, conforme o destino recebido.
4. Tente o painel do outro perfil: a resposta será `403`.
5. Execute `POST /sair` e repita o acesso: a resposta será `401`.
6. Tente entrar com senha errada ou usuário inexistente: ambos retornam
   `401` e `E-mail ou senha incorretos.`.

| Operação | Resultado |
|---|---|
| `POST /login` | Autentica, cria sessão e informa o destino conforme o perfil |
| `GET /area-aluno` | Exibe os dados públicos do aluno autenticado |
| `GET /painel-coordenador` | Exibe os dados públicos do coordenador autenticado |
| `POST /sair` | Revoga a sessão no servidor e remove o cookie; resposta `204` |

## Organização

- `aplicacao/autenticacao.py`: `Usuario`, `Perfil`, persistência e verificação da senha.
- `aplicacao/sessoes.py`: criação, expiração e encerramento das sessões.
- `aplicacao/api.py`: rotas, cookies, validação e autorização por perfil.
- `aplicacao/principal.py`: configuração e criação da aplicação.
- `aplicacao/criar_usuario.py`: preparação administrativa dos usuários.
- `tests/`: testes automatizados de aceitação, persistência e execução.

As classes de usuários não dependem do FastAPI, conforme a documentação do projeto.
Senhas usam PBKDF2-HMAC-SHA256, 600 mil iterações e sal aleatório individual;
a comparação dos hashes usa `compare_digest`. Consultas SQLite são parametrizadas.

## Configuração e limites da entrega

`BANCO_USUARIOS` permite mudar o caminho do SQLite; o padrão é `usuarios.sqlite3`
na pasta de execução. Use o mesmo caminho na preparação de usuários e no servidor.

O cookie tem `HttpOnly`, `SameSite=Strict` e validade de uma hora. `Secure` é ativado
por padrão; apenas `AMBIENTE=desenvolvimento` permite a demonstração via HTTP local.
Fora da demonstração, use HTTPS e remova essa variável ou defina outro valor.

As sessões ficam na memória de **um processo**: reiniciar o servidor encerra todas.
O armazenamento dos usuários persiste no SQLite. A implantação em múltiplos processos
exigiria um armazenamento compartilhado de sessões. Limitação de tentativas de login
e demais medidas de implantação não foram implementadas nesta atividade.

Na execução validada, os testes emitiram um aviso de descontinuação da integração
Starlette/httpx. Os 26 testes passaram; o aviso não indica falha funcional.
