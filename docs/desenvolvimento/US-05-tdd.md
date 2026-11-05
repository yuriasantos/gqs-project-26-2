# Relatório — US-05 com TDD

## Escopo e rastreabilidade

História: [US-05 — Fazer login](../requisitos/historias/US-05-fazer-login.md).
Implementação em Python com FastAPI, conforme as decisões do projeto.

| Critério | Implementação | Testes em `tests/test_login.py` |
|---|---|---|
| US-05 c1: entrar na área conforme o perfil | `entrar`, `acessar_area` e `RepositorioUsuarios.autenticar` | `test_c1_login_abre_area_do_perfil`, `test_c1_aluno_nao_acessa_painel_do_coordenador` |
| US-05 c2: recusa genérica | `entrar` e `recusar_dados_invalidos` | `test_c2_recusa_credenciais_com_mesma_mensagem` |
| US-05 c3: encerrar a sessão | `sair` e `GerenciadorSessoes.encerrar` | `test_c3_sair_revoga_sessao_inclusive_para_token_copiado`, `test_c3_sair_sem_sessao_pode_ser_repetido` |

Recuperação de senha permanece fora do escopo. As áreas devolvem JSON; não foi
criada uma interface gráfica própria. A demonstração usa a documentação interativa da API.

## Ciclos executados

Os testes foram escritos, executados e commitados antes do código correspondente.
Cada etapa vermelha tem uma falha observada; as etapas verdes executaram a suíte
completa existente naquele momento. As contagens incluem os casos parametrizados.

| Ciclo | Vermelho observado | Verde observado |
|---|---|---|
| 1 — Login e perfil | Erro de coleta: pacote `aplicacao` ainda inexistente | 3 testes passaram |
| 2 — Credenciais inválidas | 3 falharam e 9 passaram: campos ausentes devolviam `422` | 12 testes passaram |
| 3 — Saída e revogação | 4 falharam e 14 passaram: saída inexistente e token anterior ainda aceito | 18 testes passaram |
| 4 — Validade e isolamento | 1 falhou e 22 passaram: relógio para expiração ainda não suportado | 23 testes passaram |
| 5 — Preparação e execução | 3 falharam: módulos de preparação e execução ainda inexistentes | 26 testes passaram |

No primeiro ciclo, foi necessário preparar o ambiente virtual e permitir o acesso
do pytest à pasta temporária do Windows. Essa falha de ambiente foi resolvida antes
de considerar a implementação verde.

## Refatoração

O controle de sessões foi separado das rotas durante o ciclo 4. Após os cinco ciclos,
a mensagem de erro e os atributos dos cookies foram centralizados, retirando duplicações
entre criação e exclusão do cookie. A suíte foi executada novamente para verificar
que o comportamento continuou o mesmo.

## Verificações adicionais

- Credenciais incorretas, vazias, ausentes, nulas, com tipo inválido e tentativa de injeção SQL.
- Visitante e token inventado não acessam as áreas protegidas.
- Token copiado não pode ser reutilizado após logout, substituição ou expiração.
- Sair de um navegador não encerra a sessão de outro navegador.
- Validade de uma hora verificada com relógio controlado, sem aguardar tempo real.
- Senhas iguais geram hashes distintos e não ficam em texto puro no SQLite.
- Usuários persistem ao reabrir o repositório SQLite.
- Cookie seguro por padrão e modo HTTP local explicitamente configurado.
- Preparação de usuário sem imprimir a senha.

Os testes usam SQLite temporário e clientes da aplicação FastAPI, sem acessar
contas externas ou modificar dados reais.

## Consultar o histórico

```powershell
git log --oneline --reverse main..funcionalidade/login-com-tdd
git show 79c1ee9
git show f0a1ae8
```

Os dois últimos comandos exibem o primeiro teste e a implementação subsequente.
Os commits vermelhos são registros intencionais do TDD; a ponta final da branch
contém a implementação com a suíte passando.

## Executar novamente

```powershell
.\.venv\Scripts\python -m pytest -q
git diff --check
```

Ambiente validado: Windows, Python 3.14.4. Dependências diretas fixadas em
`requirements.txt` e `requirements-dev.txt`. A suíte apresenta um aviso de
descontinuação da integração Starlette/httpx, sem falhas nos testes.
