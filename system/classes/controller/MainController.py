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
