'''
Arquivo referente a classe CarroController
'''
import logging
from classes.model.database.Carro_db import *
from classes.model.Carro import *

class Carro_controller(object):
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
        retorno = carro.validar()
        if retorno['valido']:
            carro_db = Carro_db()
            return carro_db.inserir(carro)
        return retorno
    #----------------------------------------------------------------------------

    @classmethod
    def listar(cls):
        '''
        Metodo responsavel por retornar a lista de carros vindo da classe CarroDB
        '''
        carro_db = Carro_db()
        return carro_db.listar()
    #----------------------------------------------------------------------------

    @classmethod
    def listar_disponiveis(cls):
        '''
        Metodo responsavel por retornar a lista de carros vindo da classe CarroDB
        '''
        carro_db = Carro_db()
        return carro_db.listar_disponiveis()
    #----------------------------------------------------------------------------

    @classmethod
    def get_carro(cls, carro_json):
        '''
        Metodo resposavel por receber um JSON vindo da API e tranformar
        num objeto Carro
        :param carro_json:
        :return: Carro
        '''
        logging.debug('iniciou get_carro')
        carro = Carro()
        carro.set_placa(carro_json['placa'])
        carro.set_ano_fabricacao(carro_json['ano_fabricacao'])
        carro.set_cor(carro_json['cor'])
        carro.set_qtde_portas(carro_json['qtde_portas'])
        carro.set_quilometragem(carro_json['quilometragem'])
        carro.set_valor_diaria(carro_json['valor_diaria'])
        if 'id' in carro_json:
            carro.set_id(carro_json['id'])
        logging.debug('get_carro concluido com sucesso')
        return carro
    #----------------------------------------------------------------------------

    @classmethod
    def get_carro_by_id(cls, id):
        '''
        Metodo resposavel por receber um JSON vindo da API e tranformar
        num objeto Carro
        :param carro_json:
        :return: Carro
        '''
        logging.debug('iniciou get_carro_by_id')
        carro_db = Carro_db()
        carro = carro_db.get(id)
        return carro
    #----------------------------------------------------------------------------

    @classmethod
    def alterar(cls, carro):
        retorno = carro.validar()
        if retorno['valido']:
            carro_db = Carro_db()
            return carro_db.alterar(carro)
        return retorno
    # ----------------------------------------------------------------------------

    @classmethod
    def excluir(cls, id):
        carro_db = Carro_db()
        return carro_db.excluir(id)
    # ----------------------------------------------------------------------------
