'''
Arquivo referente a classe CarroController
'''
import classes.model.database.CarroDB as cdb
from classes.view import CarroView as cv

class CarroController(object):
    '''
    Classe responsavel para execucao dos metodos para manipulacao dos dados da classe carro
    '''

    @classmethod
    def incluir(cls, carro):
        '''
        Metodo responsavel pela execucao do metodo inserir da classe CarroDB
        :param carro:
        '''
        carro_db = cdb.CarroDB()
        carro_db.inserir(carro)
    #----------------------------------------------------------------------------

    @classmethod
    def listar(cls):
        '''
        Metodo responsavel por retornar a lista de carros vindo da classe CarroDB
        '''
        carro_db = cdb.CarroDB()
        carro_view = cv.CarroView()
        carro_view.apresentarListaCarro(carro_db.listar())
    #----------------------------------------------------------------------------
