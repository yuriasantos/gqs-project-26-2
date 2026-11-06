"""Testes da Inscricao — US-08 (confirmar pagamento) e US-09 (links de acesso).

Cada teste cobre um critério de aceitação, citado como `US-NN cN`,
seguindo a matriz história → método → teste do passo 3.
"""

from datetime import date, datetime

import pytest

from dominio import (
    Curso,
    Inscricao,
    Modulo,
    PagamentoJaConfirmado,
    StatusInscricao,
    Usuario,
)


def nova_inscricao() -> Inscricao:
    aluno = Usuario(nome="Ana Silva", email="ana@email.com")
    curso = Curso(modulos=[Modulo(titulo="Módulo 1", link="https://meet.google.com/abc")])
    return Inscricao(aluno=aluno, curso=curso, data=datetime(2026, 11, 5, 10, 0))


class TestUS08:

    def test_us08_c1_inscrito_expoe_nome_email_data_e_status(self):
        """US-08 c1 — o coordenador vê nome, e-mail, data e status do inscrito."""
        inscricao = nova_inscricao()

        assert inscricao.aluno.nome == "Ana Silva"
        assert inscricao.aluno.email == "ana@email.com"
        assert inscricao.data == datetime(2026, 11, 5, 10, 0)
        assert inscricao.status is StatusInscricao.AGUARDANDO_PAGAMENTO

    def test_us08_c2_confirmar_muda_status_e_libera_acesso(self):
        """US-08 c2 — confirmar muda o status e libera o acesso aos links."""
        inscricao = nova_inscricao()

        inscricao.confirmar_pagamento()

        assert inscricao.status is StatusInscricao.PAGAMENTO_CONFIRMADO
        assert inscricao.acesso_liberado() is True
        assert inscricao.links_liberados() == ["https://meet.google.com/abc"]

    def test_us08_c3_nao_confirma_duas_vezes(self):
        """US-08 c3 — segunda confirmação é recusada, sem reenvio implícito."""
        inscricao = nova_inscricao()
        inscricao.confirmar_pagamento()

        with pytest.raises(PagamentoJaConfirmado):
            inscricao.confirmar_pagamento()

    def test_us08_c4_registra_se_e_quando_email_saiu(self):
        """US-08 c4 — registra se e quando o e-mail de acesso foi enviado."""
        inscricao = nova_inscricao()
        assert inscricao.acesso_enviado_em is None

        enviado_em = datetime(2026, 11, 6, 9, 30)
        inscricao.registrar_envio_acesso(enviado_em)

        assert inscricao.acesso_enviado_em == enviado_em


class TestUS09:

    def test_us09_c3_aguardando_pagamento_nao_ve_links(self):
        """US-09 c3 — aguardando pagamento, o aluno não vê os links."""
        inscricao = nova_inscricao()

        assert inscricao.acesso_liberado() is False
        assert inscricao.links_liberados() == []

    def test_us09_c2_confirmado_ve_links_e_datas_dos_modulos(self):
        """US-09 c2 — confirmado, o aluno vê links (e, no síncrono, datas)."""
        data_aula = date(2026, 11, 20)
        aluno = Usuario(nome="Ana Silva", email="ana@email.com")
        curso = Curso(modulos=[
            Modulo(titulo="Aula 1", link="https://meet.google.com/aula1", data=data_aula),
            Modulo(titulo="Aula 2", link="https://meet.google.com/aula2", data=data_aula),
        ])
        inscricao = Inscricao(aluno=aluno, curso=curso, data=datetime(2026, 11, 5))

        inscricao.confirmar_pagamento()

        assert inscricao.links_liberados() == [
            "https://meet.google.com/aula1",
            "https://meet.google.com/aula2",
        ]
        assert [m.data for m in inscricao.curso.modulos] == [data_aula, data_aula]

    def test_us09_c4_links_sempre_atualizados(self):
        """US-09 c4 — módulo acrescentado depois aparece na área do aluno."""
        inscricao = nova_inscricao()
        inscricao.confirmar_pagamento()

        assert inscricao.links_liberados() == ["https://meet.google.com/abc"]

        inscricao.curso.modulos.append(
            Modulo(titulo="Módulo 2", link="https://youtube.com/novo")
        )
        inscricao.curso.modulos[0].link = "https://meet.google.com/alterado"

        assert inscricao.links_liberados() == [
            "https://meet.google.com/alterado",
            "https://youtube.com/novo",
        ]
