'''
Testes unitario da classe CarroDB
'''
import unittest

from classes.model import Carro as Carro
from classes.model.database import CarroDB as CarroDB

class MyTestCase(unittest.TestCase):

    '''
    Testando a inclusão do carro
    '''
    def test_inclusao_correta(self):
        carro = Carro.Carro()
        carro.set_placa('TST0001')
        carro.set_cor('BRANCA')
        carro.set_qtde_portas(2)
        carro.set_ano_fabricacao(2010)
        carro.set_quilometragem(1500)
        carro.set_valor_diaria(200)
        carro_db = CarroDB.CarroDB(True)
        retorno = carro_db.inserir(carro)
        id = int(retorno['id'])
        self.assertGreater(id,0)


if __name__ == '__main__':
    unittest.main()
