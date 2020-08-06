import unittest

from classes.model.Carro import Carro

class Test_Carro(unittest.TestCase):
    '''
    Classe responsável pelo testes unitários da classe Carro
    python -m unittest discover -s tests/model
    '''

    def test_validacao_carro_sem_dados(self):
        '''
        Teste para conferir se um objeto carro sem nenhum dado
        atribuído retornará as críticas esperadas
        '''
        carro = Carro()
        erros = carro.validar()
        self.assertGreater(len(erros),0)
