'''
Arquivo da classe LocacaoDB
'''
#from classes.model.Cliente import Cliente
#from classes.model.Carro import Carro
#from classes.model.Locacao import Locacao
from classes.model.database import Connection

class LocacaoDB(Connection.Connection):
    '''
    Classe responsavel pela manipulacao dos dados da Locacao no banco de dados
    '''

    # esse decorator podera ser retirado quando a classe estivar pronta
    # def pesquisar(self, cliente, carro): # assinatura original
    @classmethod
    def pesquisar(cls):
        '''
        Metodo responsavel por pesquisar uma locacao com base no cliente ou no
        carro.
        :param cliente:
        :param carro:
        :return: Um objeto Locacao
        '''
        return None
    # ----------------------------------------------------------------------------------------

    def registrar(self, locacao):
        '''
        Metodo responsavel pela gravacao da locacao na base de dados
        :param locacao:
        '''
    # ----------------------------------------------------------------------------------------

    def devolucao(self, locacao):
        '''
        Metodo responsavel por efetuar o registro da devolucao na base de dados
        :param locacao:
        '''
    # ----------------------------------------------------------------------------------------
