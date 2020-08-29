'''
Arquivo referente a antiga classe MainController que faz a interface com
os metodos disponibilizados pela API
'''
from classes.controller.CarroController import *

# 3rd party modules
from flask import make_response, abort

def inserir_carro(carro):
    '''
    :param carro:
    :return:
    #print(carro)
    objeto_carro = CarroController.get_carro(carro)
    #print(carro_)
    retorno = CarroController.incluir(objeto_carro)
    if 'erro' in retorno:
        return abort(206,retorno['erro'])
    return make_response(retorno, 201)
    '''
    return make_response('Funcionalidade indisponível',404)

def listar_carros():
    '''
    GET api/carro
    Metodo para retornar a lista de carros do sistema
    :return: Lista de carro
    '''
    return make_response('Funcionalidade indisponível',404)

def atualizar_carro(carro):
    '''
    PUT api/carro
    Metodo preencher atualizar o carro no sistema
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def get_carro(id):
    '''
    GET api/carro/{id}
    Metodo para recuperar o carro do id passado como parametro
    :param id: 
    :return: 
    '''
    return make_response('Funcionalidade indisponível',404)

def deletar_carro(id):
    '''
    DELETE api/carro/{id}
    Metodo para exclusao do carro do id passado como parametro
    :param id: 
    :return: 
    '''
    return make_response('Funcionalidade indisponível',404)

def listar_carros_disponiveis():
    '''
    GET api/carro/disponiveis
    Metodo para recuperar todos os carros disponiveis para locacao
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def listar_clientes():
    '''
    GET api/cliente
    Metodo para recuperar todos os clientes da base de dados
    :return: Lista de clientes
    '''
    return make_response('Funcionalidade indisponível',404)

def incluir_cliente(cliente):
    '''
    POST api/cliente
    Metodo para realizar a inclusao do cliente no sistema
    :param cliente:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def atualizar_cliente(cliente):
    '''
    PUT api/cliente
    Metodo para realizar a atualizacao do cliente no sistema
    :param cliente:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def get_cliente(id):
    '''
    GET api/cliente/{id}
    Metodo para recuperar o cliente do id passado como parametro
    :param id:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def excluir_cliente(id):
    '''
    DELETE api/cliente/{id}
    Metodo para realizar a excluisao do cliente no sistema
    :param id:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def incluir_locacao(locacao):
    '''
    POST api/locacao
    Metodo para realizar a inclusao da locacao no sistema
    :param locacao:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def atualizar_locacao(locacao):
    '''
    PUT api/locacao
    Metodo para atualizar a locacao no sistema
    :param locacao:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def get_locacao_por_id(id):
    '''
    GET api/locacao/{id}
    Metodo para recuperar a locacao pelo seu id.
    :param id:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def calcular_locacao(id):
    '''
    GET api/locacao/calculo/{id}
    Metodo para realizar o calculo monetario da locacao
    :param id:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)

def get_locacao_por_cpf_ou_placa(cpf_placa):
    '''
    GET api/locacao/cpf-placa/{cpf_placa}
    Metodo para recuperar a locacao com base no CPF ou na PLACA do carro.
    :param cpf_placa:
    :return:
    '''
    return make_response('Funcionalidade indisponível',404)
