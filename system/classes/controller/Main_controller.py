'''
Arquivo referente a antiga classe MainController que faz a interface com
os metodos disponibilizados pela API
'''
from __future__ import print_function
from classes.controller.Carro_controller import *
from flask import make_response, abort
from util import util

logger = util.start_loggin()

def inserir_carro(carro):
    '''
    :param carro:
    :return:
    '''
    logger.debug('Chamou o inserir_carro')
    try:
        objeto_carro = Carro_controller.get_carro(carro)
        retorno = Carro_controller.incluir(objeto_carro)
        if 'erro' in retorno:
            return abort(206, retorno['erro'])
        if 'valido' in retorno:
            if not retorno['valido']:
                return make_response(retorno, 206)
        logger.debug('inserir_carro executado com sucesso')
        return make_response(retorno, 201)
    except Exception as e:
        logger.exception('Falha no inserir_carro', e)
        return make_response('Erro interno no servidor', 503)

def listar_carros():
    '''
    GET api/carro
    Metodo para retornar a lista de carros do sistema
    :return: Lista de carro
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def atualizar_carro(carro):
    '''
    PUT api/carro
    Metodo preencher atualizar o carro no sistema
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def get_carro(id):
    '''
    GET api/carro/{id}
    Metodo para recuperar o carro do id passado como parametro
    :param id: 
    :return: 
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def deletar_carro(id):
    '''
    DELETE api/carro/{id}
    Metodo para exclusao do carro do id passado como parametro
    :param id: 
    :return: 
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def listar_carros_disponiveis():
    '''
    GET api/carro/disponiveis
    Metodo para recuperar todos os carros disponiveis para locacao
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def listar_clientes():
    '''
    GET api/cliente
    Metodo para recuperar todos os clientes da base de dados
    :return: Lista de clientes
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def incluir_cliente(cliente):
    '''
    POST api/cliente
    Metodo para realizar a inclusao do cliente no sistema
    :param cliente:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def atualizar_cliente(cliente):
    '''
    PUT api/cliente
    Metodo para realizar a atualizacao do cliente no sistema
    :param cliente:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def get_cliente(id):
    '''
    GET api/cliente/{id}
    Metodo para recuperar o cliente do id passado como parametro
    :param id:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def excluir_cliente(id):
    '''
    DELETE api/cliente/{id}
    Metodo para realizar a excluisao do cliente no sistema
    :param id:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def incluir_locacao(locacao):
    '''
    POST api/locacao
    Metodo para realizar a inclusao da locacao no sistema
    :param locacao:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def atualizar_locacao(locacao):
    '''
    PUT api/locacao
    Metodo para atualizar a locacao no sistema
    :param locacao:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def get_locacao_por_id(id):
    '''
    GET api/locacao/{id}
    Metodo para recuperar a locacao pelo seu id.
    :param id:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def calcular_locacao(id):
    '''
    GET api/locacao/calculo/{id}
    Metodo para realizar o calculo monetario da locacao
    :param id:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)

def get_locacao_por_cpf_ou_placa(cpf_placa):
    '''
    GET api/locacao/cpf-placa/{cpf_placa}
    Metodo para recuperar a locacao com base no CPF ou na PLACA do carro.
    :param cpf_placa:
    :return:
    '''
    try:
        return make_response('Funcionalidade indisponível', 404)
    except Exception as e:
        logger.exception('Falha na listagem dos carros', e)
        return make_response('Erro interno no servidor', 503)
