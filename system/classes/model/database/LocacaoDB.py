from classes.model.Cliente import Cliente
from classes.model.Carro import Carro
from classes.model.Locacao import Locacao

class LocacaoDB():
    '''
    Classe responsável pela manipulação dos dados da Locação no banco de dados
    '''

    def pesquisar(self,cliente,carro):
        '''
        Método responsável por pesquisar uma locação com base no cliente ou no
        carro.
        :param cliente:
        :param carro:
        :return: Um objeto Locação
        '''
    # ----------------------------------------------------------------------------------------

    def registrar(self,locacao):
        '''
        Método responsável pela gravação da locação na base de dados
        :param locacao:
        :return:
        '''
    # ----------------------------------------------------------------------------------------

    def devolucao(self,locacao):
        '''
        Método responsável por efetuar o registro da devolução na base de dados
        :param locacao:
        :return:
        '''
    # ----------------------------------------------------------------------------------------
