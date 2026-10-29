
import unittest
from decimal import Decimal

from src.calculos import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        """Cria uma calculadora nova antes de cada teste."""
        self.calc = Calculadora()

    def digitar(self, sequencia):
        """
        Simula os botões pressionados na ordem recebida.

        Exemplo:
        self.digitar(["1", "0", "+", "2", "="])
        """
        for tecla in sequencia:
            self.calc.pressionar(tecla)

        return self.calc.display

    def verificar(self, sequencia, esperado):
        """Executa uma sequência e compara o visor."""
        resultado = self.digitar(sequencia)
        self.assertEqual(resultado, esperado)

    # ==========================================
    # 1. OPERAÇÕES MATEMÁTICAS BÁSICAS
    # ==========================================

    def test_01_soma(self):
        self.verificar(
            ["5", "+", "3", "="], "8"
        )

    def test_02_subtracao(self):
        self.verificar(
            ["9", "-", "4", "="], "5"
        )

    def test_03_multiplicacao(self):
        self.verificar(
            ["6", "×", "7", "="], "42"
        )

    def test_04_divisao(self):
        self.verificar(
            ["8", "÷", "2", "="], "4"
        )

    def test_05_divisao_decimal(self):
        self.verificar(
            ["7", "÷", "2", "="], "3,5"
        )

    def test_06_resultado_negativo(self):
        self.verificar(
            ["3", "-", "8", "="], "-5"
        )

    # ==========================================
    # 2. OPERAÇÕES ENCADEADAS
    # ==========================================

    def test_07_soma_encadeada(self):
        self.verificar(
            ["1", "0", "+", "2", "0", "+", "3", "0", "="],
            "60"
        )

    def test_08_operacoes_mistas(self):
        self.verificar(
            ["1", "0", "+", "5", "×", "2", "="],
            "30"
        )

    def test_09_divisoes_encadeadas(self):
        self.verificar(
            ["8", "0", "÷", "2", "÷", "4", "="],
            "10"
        )

    def test_10_igual_repetido(self):
        self.verificar(
            ["5", "+", "2", "=", "=", "="],
            "11"
        )

    def test_11_operacao_apos_igual(self):
        self.verificar(
            ["5", "+", "5", "=", "×", "2", "="],
            "20"
        )

    def test_12_operador_substituido(self):
        self.verificar(
            ["8", "+", "×", "2", "="],
            "16"
        )

    # ==========================================
    # 3. OPERAÇÕES AVANÇADAS
    # ==========================================

    def test_13_quadrado(self):
        self.verificar(
            ["5", "x²"], "25"
        )

    def test_14_quadrado_negativo(self):
        self.verificar(
            ["5", "+/-", "x²"], "25"
        )

    def test_15_raiz_quadrada(self):
        self.verificar(
            ["9", "²√x"], "3"
        )

    def test_16_raiz_decimal(self):
        self.verificar(
            ["2", ",", "2", "5", "²√x"], "1,5"
        )

    def test_17_inverso(self):
        self.verificar(
            ["4", "1/x"], "0,25"
        )

    def test_18_inverter_sinal(self):
        self.verificar(
            ["7", "+/-"], "-7"
        )

    def test_19_inverter_sinal_duas_vezes(self):
        self.verificar(
            ["7", "+/-", "+/-"], "7"
        )

    def test_20_porcentagem_simples(self):
        self.verificar(
            ["5", "0", "%"], "0,5"
        )

    def test_21_porcentagem_soma(self):
        self.verificar(
            ["1", "0", "0", "+", "1", "0", "%", "="],
            "110"
        )

    def test_22_porcentagem_subtracao(self):
        self.verificar(
            ["2", "0", "0", "-", "1", "0", "%", "="],
            "180"
        )

    def test_23_porcentagem_multiplicacao(self):
        self.verificar(
            ["2", "0", "0", "×", "1", "0", "%", "="],
            "20"
        )

    # ==========================================
    # 4. NÚMEROS DECIMAIS
    # ==========================================

    def test_24_soma_decimal(self):
        self.verificar(
            ["0", ",", "1", "+", "0", ",", "2", "="],
            "0,3"
        )

    def test_25_virgula_repetida(self):
        self.verificar(
            ["1", ",", ",", "5"], "1,5"
        )

    def test_26_virgula_apos_operador(self):
        self.verificar(
            ["5", "+", ",", "5", "="],
            "5,5"
        )

    def test_27_zeros_iniciais(self):
        self.verificar(
            ["0", "0", "0", "5"], "5"
        )

    # ==========================================
    # 5. LIMPEZA E EDIÇÃO
    # ==========================================

    def test_28_limpar_tudo(self):
        self.verificar(
            ["5", "+", "3", "C"], "0"
        )

        self.assertEqual(self.calc.historico, "")
        self.assertIsNone(self.calc.operador)
        self.assertIsNone(self.calc.acumulado)

    def test_29_limpar_entrada(self):
        self.verificar(
            ["5", "+", "3", "CE", "2", "="],
            "7"
        )

    def test_30_ce_apos_igual(self):
        self.verificar(
            ["5", "+", "3", "=", "CE"],
            "0"
        )

        self.assertEqual(self.calc.historico, "")

    def test_31_backspace(self):
        self.verificar(
            ["1", "2", "3", "⌫"],
            "12"
        )

    def test_32_backspace_ultimo_digito(self):
        self.verificar(
            ["5", "⌫"], "0"
        )

    def test_33_novo_numero_apos_igual(self):
        self.verificar(
            ["5", "+", "3", "=", "9"],
            "9"
        )

    # ==========================================
    # 6. TRATAMENTO DE ERROS
    # ==========================================

    def test_34_divisao_por_zero(self):
        self.verificar(
            ["5", "÷", "0", "="],
            "Erro"
        )

    def test_35_raiz_negativa(self):
        self.verificar(
            ["9", "+/-", "²√x"],
            "Erro"
        )

    def test_36_inverso_de_zero(self):
        self.verificar(
            ["0", "1/x"],
            "Erro"
        )

    def test_37_recuperacao_apos_erro(self):
        self.verificar(
            ["5", "÷", "0", "=", "7", "+", "2", "="],
            "9"
        )

    # ==========================================
    # 7. HISTÓRICO E ESTADO
    # ==========================================

    def test_38_historico_soma(self):
        self.digitar(["5", "+", "3", "="])

        self.assertEqual(
            self.calc.historico,
            "5 + 3 ="
        )

    def test_39_estado_inicial(self):
        self.assertEqual(self.calc.display, "0")
        self.assertEqual(self.calc.historico, "")
        self.assertIsNone(self.calc.acumulado)
        self.assertIsNone(self.calc.operador)
        self.assertFalse(self.calc.erro)


# ==========================================
# EXECUÇÃO DOS TESTES
# ==========================================

if __name__ == "__main__":

    print("=" * 55)
    print("   TESTES AUTOMATIZADOS DA CALCULADORA")
    print("=" * 55)

    unittest.main(verbosity=2)
