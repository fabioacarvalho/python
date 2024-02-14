import unittest
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    # Todos os testes devem iniciar com a palavra test, se não não serão executados

    def test_soma_5_mais_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 15)

    def test_soma_5_mais_5_deve_retornar_15(self):
        self.assertEqual(soma(5, 10), 15)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (10, 15, 25),
            (5, 10,  15),
            (2, 2, 4),
            (2, 2, 5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_retorna_erro(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

unittest.main(verbosity=2)
