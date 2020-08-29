'''
Arquivo referente a classe CarroController
'''
from classes.model.database.CarroDB import *
from classes.model.Carro import *

class CarroController(object):
    '''
    Classe responsavel para execucao dos metodos para manipulacao dos dados da classe carro
    '''

    @classmethod
    def incluir(cls, carro):
        '''
        Metodo responsavel pela execucao do metodo inserir da classe CarroDB
        :param carro:
        :return Dicionario com o ID do carro inserido ou mensagem de erro
        '''
        carro_db = CarroDB()
        return carro_db.inserir(carro)
    #----------------------------------------------------------------------------

    @classmethod
    def listar(cls):
        '''
        Metodo responsavel por retornar a lista de carros vindo da classe CarroDB
        '''
        carro_db = CarroDB()
        #carro_view.apresentarListaCarro(carro_db.listar())
    #----------------------------------------------------------------------------

    @classmethod
    def get_carro(cls,carro_json):
        '''
        Metodo resposavel por receber um JSON vindo da API e tranformar
        num objeto Carro
        :param carro_json:
        :return: Carro
        '''
        carro = Carro()
        carro.set_placa(carro_json['placa'])
        carro.set_ano_fabricacao(carro_json['ano_fabricacao'])
        carro.set_cor(carro_json['cor'])
        carro.set_qtde_portas(carro_json['qtde_portas'])
        carro.set_quilometragem(carro_json['quilometragem'])
        carro.set_valor_diaria(carro_json['valor_diaria'])
        return carro


