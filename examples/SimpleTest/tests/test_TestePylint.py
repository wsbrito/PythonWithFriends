import unittest

from classes import TestePylint as teste

class Test_TestePylint(unittest.TestCase):

    def test_soma_correta(self):
        t = teste.TestePylint()
        resultado = t.realizar_soma(3,3)
        self.assertEqual(resultado,6)

    def test_soma_incorreta(self):
        t = teste.TestePylint()
        resultado = t.realizar_soma(3,7)
        self.assertNotEqual(resultado,10)
