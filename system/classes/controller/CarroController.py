import classes.model.database.CarroDB as cdb
from classes.view import CarroView as cv

class CarroController():
    '''
    Classe responsável para execução dos métodos para manipulação dos dados da classe carro
    '''

    def incluir(self,carro):
        '''
        Método responsável pela execução do método inserir da classe CarroDB
        :param carro:
        :return:
        '''
        carroDB = cdb.CarroDB()
        carroDB.inserir(carro)
    #----------------------------------------------------------------------------

    def listar(self):
        '''
        Método responsável por retornar a lista de carros vindo da classe CarroDB
        :return:
        '''
        carroDB = cdb.CarroDB()
        carroView = cv.CarroView()
        carroView.apresentarListaCarro(carroDB.listar())
    #----------------------------------------------------------------------------
