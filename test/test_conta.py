from src.conta import Conta
import pytest


class TestConta:

    @pytest.fixture()
    def conta_ciana(self):
        conta_ciana = Conta(123, "Ciana", 100.0, 1000.0)
        return conta_ciana

    @pytest.fixture()
    def conta_jom(self):
        conta_jom = Conta(345, "Jom", 200.0, 2000.0)
        return conta_jom

    def test_nao_pode_sacar_um_valor_maior_que_o_valor_disponivel_para_saque(self, conta_ciana):
        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.saca(1300.0)

    def test_pode_sacar_se_tiver_saldo(self, conta_ciana):
        conta_ciana.saca(50.0)
        assert conta_ciana.saldo == 50.0

    def test_nao_pode_sacar_um_valor_negativo(self, conta_ciana):
        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.saca(-100.0)

    def test_pode_sacar_mais_do_que_o_saldo_se_tiver_limite(self, conta_ciana):
        conta_ciana.saca(500.0)
        assert conta_ciana.saldo == -400.0

    def test_nao_pode_depositar_um_valor_negativo(self, conta_ciana):
        """O with(pytest.raises(NOME_+DA_EXCECAO)) verifica se um erro foi lançado
        pela instruções executadas dentro do with
        """
        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.deposita(-500.0)

    def test_apos_o_deposito_de_um_valor_positivo_este_valor_deve_ser_somado_ao_saldo(self, conta_ciana):
        conta_ciana.deposita(500.0)
        assert conta_ciana.saldo == 600.0

    def test_nao_pode_transferir_numero_negativo(self, conta_ciana, conta_jom):
        """ não pode transferir numero negativo """

        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.transfere(-200.0, conta_jom)

    def test_o_valor_de_transferencia_nao_pode_exceder_o_valor_disponivel_para_saque_da_conta_origem(self,
                                                                                                     conta_ciana,
                                                                                                     conta_jom):
        """o valor de transferencia não pode exceder o valor disponivel para saque da conta origem """

        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.transfere(1200.0, conta_jom)

    def test_nao_pode_fazer_uma_transferencia_com_valor_acima_do_limite_de_transferencia(self, conta_ciana, conta_jom):
        """ não pode fazer uma transferencia com valor acima do limite de transferencia (10000.0) """

        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.deposita(15000.0)
            conta_ciana.transfere(10100.0, conta_jom)

    def test_o_limite_da_conta_nao_pode_ser_negativo(self, conta_ciana):
        with(pytest.raises(ValueError)) as excecao:
            conta_ciana.limite = -100.0

    def test_altera_o_limite_da_conta(self,conta_ciana):
        conta_ciana.limite = 5000.0
        conta_ciana.saca(5100.0)
        assert conta_ciana.saldo == -5000.0
