import unittest
import math
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada


class TestCalculadora(unittest.TestCase):

    # --- Testes de Adição ---
    def test_somar_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(100, 250), 350)

    def test_somar_numeros_negativos(self):
        self.assertEqual(somar(-2, -3), -5)
        self.assertEqual(somar(-10, 5), -5)
        self.assertEqual(somar(10, -5), 5)

    def test_somar_com_zero(self):
        self.assertEqual(somar(0, 0), 0)
        self.assertEqual(somar(7, 0), 7)
        self.assertEqual(somar(0, 7), 7)

    def test_somar_decimais(self):
        self.assertAlmostEqual(somar(1.5, 2.3), 3.8)
        self.assertAlmostEqual(somar(0.1, 0.2), 0.3)

    # --- Testes de Subtração ---
    def test_subtrair_numeros_positivos(self):
        self.assertEqual(subtrair(10, 4), 6)
        self.assertEqual(subtrair(4, 10), -6)

    def test_subtrair_numeros_negativos(self):
        self.assertEqual(subtrair(-5, -2), -3)
        self.assertEqual(subtrair(-5, 2), -7)
        self.assertEqual(subtrair(5, -2), 7)

    def test_subtrair_com_zero(self):
        self.assertEqual(subtrair(5, 0), 5)
        self.assertEqual(subtrair(0, 5), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_subtrair_decimais(self):
        self.assertAlmostEqual(subtrair(5.5, 2.2), 3.3)

    # --- Testes de Multiplicação ---
    def test_multiplicar_numeros_positivos(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(7, 8), 56)

    def test_multiplicar_numeros_negativos(self):
        self.assertEqual(multiplicar(-3, 4), -12)
        self.assertEqual(multiplicar(3, -4), -12)
        self.assertEqual(multiplicar(-3, -4), 12)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(10, 0), 0)
        self.assertEqual(multiplicar(0, 10), 0)
        self.assertEqual(multiplicar(0, 0), 0)

    def test_multiplicar_por_um(self):
        self.assertEqual(multiplicar(9, 1), 9)
        self.assertEqual(multiplicar(1, 9), 9)

    def test_multiplicar_decimais(self):
        self.assertAlmostEqual(multiplicar(2.5, 4), 10.0)
        self.assertAlmostEqual(multiplicar(0.5, 0.5), 0.25)

    # --- Testes de Divisão ---
    def test_dividir_exato(self):
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(9, 3), 3.0)

    def test_dividir_com_resto(self):
        self.assertEqual(dividir(7, 2), 3.5)
        self.assertAlmostEqual(dividir(1, 3), 1 / 3)

    def test_dividir_numeros_negativos(self):
        self.assertEqual(dividir(-10, 2), -5.0)
        self.assertEqual(dividir(10, -2), -5.0)
        self.assertEqual(dividir(-10, -2), 5.0)

    def test_dividir_zero_por_numero(self):
        self.assertEqual(dividir(0, 5), 0.0)

    def test_dividir_por_zero_lanca_excecao(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)

    # --- Testes de Raiz Quadrada ---
    def test_raiz_quadrada_quadrados_perfeitos(self):
        self.assertEqual(raiz_quadrada(0), 0.0)
        self.assertEqual(raiz_quadrada(1), 1.0)
        self.assertEqual(raiz_quadrada(4), 2.0)
        self.assertEqual(raiz_quadrada(9), 3.0)
        self.assertEqual(raiz_quadrada(16), 4.0)
        self.assertEqual(raiz_quadrada(100), 10.0)

    def test_raiz_quadrada_decimais(self):
        self.assertAlmostEqual(raiz_quadrada(0.25), 0.5)
        self.assertAlmostEqual(raiz_quadrada(2.25), 1.5)

    def test_raiz_quadrada_nao_exata(self):
        self.assertAlmostEqual(raiz_quadrada(2), math.sqrt(2))
        self.assertAlmostEqual(raiz_quadrada(3), math.sqrt(3))

    def test_raiz_quadrada_numero_negativo_lanca_excecao(self):
        with self.assertRaises(ValueError):
            raiz_quadrada(-1)
        with self.assertRaises(ValueError):
            raiz_quadrada(-16)


if __name__ == "__main__":
    unittest.main()
