"""
Testes da US-04 - Criar conta de aluno (TDD).

Critérios de aceitação cobertos:
  CA1 - dados válidos -> conta criada e aluno já pode entrar no sistema
  CA2 - e-mail já cadastrado -> recusa e sugere fazer login
  CA3 - e-mail em formato inválido -> recusa
Também cobre: campos obrigatórios (nome, e-mail, senha).
"""
import pytest

from class_criar_conta_aluno import (
    CampoObrigatorioError,
    CredenciaisInvalidasError,
    EmailInvalidoError,
    EmailJaCadastradoError,
    ServicoConta,
)


@pytest.fixture
def servico():
    return ServicoConta()


NOME = "Maria da Silva"
EMAIL = "maria@email.com"
SENHA = "Senha@123"


# ---------------------------------------------------------------- CA1
class TestCriarContaComSucesso:
    def test_cria_conta_com_dados_validos(self, servico):
        aluno = servico.criar_conta(NOME, EMAIL, SENHA)

        assert aluno.nome == NOME
        assert aluno.email == EMAIL

    def test_aluno_criado_pode_entrar_no_sistema(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        aluno = servico.entrar(EMAIL, SENHA)

        assert aluno.email == EMAIL

    def test_entrar_com_senha_errada_falha(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        with pytest.raises(CredenciaisInvalidasError):
            servico.entrar(EMAIL, "senha-errada")

    def test_senha_nao_e_armazenada_em_texto_puro(self, servico):
        aluno = servico.criar_conta(NOME, EMAIL, SENHA)

        assert SENHA not in vars(aluno).values()

    def test_conta_e_registrada_no_sistema(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        assert servico.total_contas() == 1

    def test_espacos_ao_redor_do_email_sao_ignorados(self, servico):
        aluno = servico.criar_conta(NOME, "  maria@email.com  ", SENHA)

        assert aluno.email == "maria@email.com"


# ---------------------------------------------------------------- CA2
class TestEmailDuplicado:
    def test_recusa_email_ja_cadastrado(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        with pytest.raises(EmailJaCadastradoError):
            servico.criar_conta("Outra Pessoa", EMAIL, "OutraSenha@1")

    def test_mensagem_sugere_fazer_login(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        with pytest.raises(EmailJaCadastradoError, match="(?i)login"):
            servico.criar_conta("Outra Pessoa", EMAIL, "OutraSenha@1")

    def test_email_duplicado_ignora_maiusculas_e_minusculas(self, servico):
        servico.criar_conta(NOME, "maria@email.com", SENHA)

        with pytest.raises(EmailJaCadastradoError):
            servico.criar_conta(NOME, "MARIA@EMAIL.COM", SENHA)

    def test_nao_cria_segunda_conta_quando_recusa(self, servico):
        servico.criar_conta(NOME, EMAIL, SENHA)

        with pytest.raises(EmailJaCadastradoError):
            servico.criar_conta("Outra Pessoa", EMAIL, "OutraSenha@1")

        assert servico.total_contas() == 1


# ---------------------------------------------------------------- CA3
class TestEmailInvalido:
    @pytest.mark.parametrize(
        "email_invalido",
        [
            "maria",
            "maria@",
            "@email.com",
            "maria@email",
            "maria email@email.com",
            "maria@@email.com",
        ],
    )
    def test_recusa_email_com_formato_invalido(self, servico, email_invalido):
        with pytest.raises(EmailInvalidoError):
            servico.criar_conta(NOME, email_invalido, SENHA)

    def test_nao_cria_conta_quando_email_invalido(self, servico):
        with pytest.raises(EmailInvalidoError):
            servico.criar_conta(NOME, "maria@", SENHA)

        assert servico.total_contas() == 0


# ------------------------------------------------- campos obrigatórios
class TestCamposObrigatorios:
    @pytest.mark.parametrize("nome_vazio", ["", "   ", None])
    def test_nome_e_obrigatorio(self, servico, nome_vazio):
        with pytest.raises(CampoObrigatorioError, match="(?i)nome"):
            servico.criar_conta(nome_vazio, EMAIL, SENHA)

    @pytest.mark.parametrize("email_vazio", ["", "   ", None])
    def test_email_e_obrigatorio(self, servico, email_vazio):
        with pytest.raises(CampoObrigatorioError, match="(?i)e-?mail"):
            servico.criar_conta(NOME, email_vazio, SENHA)

    @pytest.mark.parametrize("senha_vazia", ["", None])
    def test_senha_e_obrigatoria(self, servico, senha_vazia):
        with pytest.raises(CampoObrigatorioError, match="(?i)senha"):
            servico.criar_conta(NOME, EMAIL, senha_vazia)

    def test_nao_cria_conta_quando_falta_campo(self, servico):
        with pytest.raises(CampoObrigatorioError):
            servico.criar_conta("", EMAIL, SENHA)

        assert servico.total_contas() == 0


# ------------------------------------------------ pendências da US (a confirmar)
@pytest.mark.skip(reason="US-04: regra mínima de senha ainda 'a confirmar'")
def test_recusa_senha_fora_da_regra_minima(servico):
    with pytest.raises(Exception):
        servico.criar_conta(NOME, EMAIL, "123")
