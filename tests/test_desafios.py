import unittest
from src.desafios import eh_palindromo, intersecao_unica, soma_intervalos

class TestDesafios(unittest.TestCase):
    def test_eh_palindromo_basico(self):
        self.assertTrue(eh_palindromo("ovo"))
        self.assertTrue(eh_palindromo("Ovo"))
        self.assertFalse(eh_palindromo("FIAP"))

    def test_eh_palindromo_frase_com_acentos(self):
        self.assertTrue(eh_palindromo("À sogra má e amargosa"))
        self.assertTrue(eh_palindromo("Socorram-me, subi no ônibus em Marrocos!"))

    def test_intersecao_unica(self):
        self.assertEqual(intersecao_unica([1,2,2,3], [2,2,4]), [2])
        self.assertEqual(intersecao_unica([], [1,2]), [])
        self.assertEqual(intersecao_unica([5,4,5], [5,5,4]), [4,5])

    def test_soma_intervalos_simples(self):
        self.assertEqual(soma_intervalos([]), 0)
        self.assertEqual(soma_intervalos([(1,2)]), 1)
        self.assertEqual(soma_intervalos([(1,5),(3,7)]), 6)
        self.assertEqual(soma_intervalos([(1,3),(3,4)]), 3)

    def test_soma_intervalos_multiplos(self):
        self.assertEqual(soma_intervalos([(1,5),(10,11),(3,7)]), 7)
        self.assertEqual(soma_intervalos([(0,1),(1,2),(2,3)]), 3)
        self.assertEqual(soma_intervalos([(1,10),(2,3),(4,8),(9,12)]), 11)

if __name__ == "__main__":
    unittest.main()
