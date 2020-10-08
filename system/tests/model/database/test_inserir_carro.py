'''
Testes unitario da classe CarroDB
'''
import unittest

from system.classes.model import Carro as c
from system.classes.model.database import Carro_db as carro_db

class Teste_inclusao_carro(unittest.TestCase):

    def get_carro_para_teste(self):
        carro = c.Carro()
        carro.set_placa('TST0001')
        carro.set_cor('#FFFF')
        carro.set_qtde_portas(2)
        carro.set_ano_fabricacao(2010)
        carro.set_quilometragem(1500)
        carro.set_valor_diaria(200)
        return carro

    '''
    Testando a inclusao correta do do carro
    '''
    def test_inclusao_correta(self):
        carro = self.get_carro_para_teste()
        carro_database = carro_db.Carro_db(True)
        retorno = carro_database.inserir(carro)
        id = int(retorno['id'])
        self.assertGreater(id, 0)

    '''
    Testando a inclusao do carro sem placa 
    '''
    def test_inclusao_carro_placa_em_branco(self):
        carro = self.get_carro_para_teste()
        carro.set_placa("")
        retorno = carro.validar()
        mensagem = retorno['placa']
        self.assertEqual(mensagem,'Placa '+chr(233)+' de preenchimento obrigat'+chr(243)+'rio')

    '''
    Testando a inclusao do carro com a placa no formato errado 
    '''
    def test_inclusao_carro_placa_errada(self):
        carro = self.get_carro_para_teste()
        carro.set_placa("A2A0976")
        retorno = carro.validar()
        mensagem = retorno['placa']
        self.assertEqual(mensagem,'A placa informada ' + chr(233) + ' inv'+chr(225)+'lida')

    '''
    Testando a inclusao do carro sem informcao da cor 
    '''
    def test_inclusao_carro_sem_cor(self):
        carro = self.get_carro_para_teste()
        carro.set_cor("")
        retorno = carro.validar()
        mensagem = retorno['cor']
        self.assertEqual(mensagem,'A cor informada ' + chr(233) + ' inv' + chr(225) + 'lida')

    '''
    Testando a inclusao do carro com a cor invalida 
    '''
    def test_inclusao_carro_cor_invalida(self):
        carro = self.get_carro_para_teste()
        carro.set_cor("#HHFFFF")
        retorno = carro.validar()
        mensagem = retorno['cor']
        self.assertEqual(mensagem,'A cor informada ' + chr(233) + ' inv' + chr(225) + 'lida')

    '''
    Testando a inclusao do carro com o ano de fabricacao negativo 
    '''
    def test_inclusao_carro_ano_fabricacao_negativo(self):
        carro = self.get_carro_para_teste()
        carro.set_ano_fabricacao(-1)
        retorno = carro.validar()
        mensagem = retorno['ano_fabricacao']
        self.assertEqual(mensagem,'Ano de fabrica' + chr(231) + chr(277) + 'o ' + chr(233) + ' deve ser superior a 1955')

    '''
    Testando a inclusao do carro com o ano de fabricacao menor que 1955 
    '''
    def test_inclusao_carro_ano_fabricacao_antes_1955(self):
        carro = self.get_carro_para_teste()
        carro.set_ano_fabricacao(1953)
        retorno = carro.validar()
        mensagem = retorno['ano_fabricacao']
        self.assertEqual(mensagem,'Ano de fabrica' + chr(231) + chr(277) + 'o ' + chr(233) + ' deve ser superior a 1955')

    '''
    Testando a inclusao do carro com o ano de fabricacao nao numerico 
    '''
    def test_inclusao_carro_ano_fabricacao_nao_numerico(self):
        carro = self.get_carro_para_teste()
        carro.set_ano_fabricacao("TESTE")
        retorno = carro.validar()
        mensagem = retorno['ano_fabricacao']
        self.assertEqual(mensagem,'Ano de fabrica'+chr(231)+chr(277)+'o '+chr(233)+' um dado num'+chr(233)+'rico')

    '''
    Testando a inclusao do carro com a quantidade de portas nao numerica 
    '''
    def test_inclusao_carro_quantidade_portas_nao_numerica(self):
        carro = self.get_carro_para_teste()
        carro.set_qtde_portas("TESTE")
        retorno = carro.validar()
        mensagem = retorno['qtde_portas']
        self.assertEqual(mensagem,'A quantidade de portas '+chr(233)+' um dado num'+chr(233)+'rico')

    '''
    Testando a inclusao do carro com a quantidades de porta zerada 
    '''
    def test_inclusao_carro_quantidade_portas_menor_que_um(self):
        carro = self.get_carro_para_teste()
        carro.set_qtde_portas(0)
        retorno = carro.validar()
        mensagem = retorno['qtde_portas']
        self.assertEqual(mensagem,'O carro deve ter pelo menos uma porta')

    '''
    Testando a inclusao do carro com a quilometragem negativa 
    '''
    def test_inclusao_carro_quilometragem_negativa(self):
        carro = self.get_carro_para_teste()
        carro.set_quilometragem(-1)
        retorno = carro.validar()
        mensagem = retorno['quilometragem']
        self.assertEqual(mensagem,'A quilometragem deve maior ou igual a zero')

    '''
    Testando a inclusao do carro com a quilometragem nao numerica 
    '''
    def test_inclusao_carro_quilometragem_negativa(self):
        carro = self.get_carro_para_teste()
        carro.set_quilometragem("TESTE")
        retorno = carro.validar()
        mensagem = retorno['quilometragem']
        self.assertEqual(mensagem,'A quilometragem '+chr(233)+' um dado num'+chr(233)+'rico')

    '''
    Testando a inclusao do carro com o valor da diaria negativo 
    '''
    def test_inclusao_carro_valor_diaria_negativo(self):
        carro = self.get_carro_para_teste()
        carro.set_valor_diaria(-1)
        retorno = carro.validar()
        mensagem = retorno['valor_diaria']
        self.assertEqual(mensagem,'O valor da di'+chr(225)+'ria '+chr(233)+' deve ser de pelo menos R$ 50,00')

    '''
    Testando a inclusao do carro com o valor da diaria zerado 
    '''
    def test_inclusao_carro_valor_diaria_zerado(self):
        carro = self.get_carro_para_teste()
        carro.set_valor_diaria(0)
        retorno = carro.validar()
        mensagem = retorno['valor_diaria']
        self.assertEqual(mensagem,'O valor da di'+chr(225)+'ria '+chr(233)+' deve ser de pelo menos R$ 50,00')

    '''
    Testando a inclusao do carro com o valor da diaria nao numerico 
    '''
    def test_inclusao_carro_valor_diaria_nao_numerico(self):
        carro = self.get_carro_para_teste()
        carro.set_valor_diaria("TESTE")
        retorno = carro.validar()
        mensagem = retorno['valor_diaria']
        self.assertEqual(mensagem,'O valor da di'+chr(225)+'ria '+chr(233)+' um dado num'+chr(233)+'rico')

if __name__ == '__main__':
    unittest.main()
