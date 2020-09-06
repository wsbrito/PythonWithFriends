'''
Arquivo com os metodos uteis para execucao da aplicacao, tais como,
enderecamento da pasta principalda aplicacao, da recuperacao dos
dados do arquivo config.json, inicializacao do log e
da criacao das base de dados para teste e execucao da aplicacao
'''
from pathlib import Path
import json
import os
import logging
import re

def get_project_root() -> Path:
    '''
    Metodo auxiliar para indicar o correto path da raiz da aplicacao.
    Util para a classe de conexao nao de perder para localizar o banco de dados.
    :return: Diretorio raiz da aplicacao
    '''
    return Path(__file__).parent.parent

def get_config_data():
    '''
    Metodo para retornar os dados do arquivos config.json
    :return: Dicionario contendo os dados do arquivo config.json
    '''
    path = get_project_root()
    with open(str(path)+"/config.json") as json_data_file:
        data = json.load(json_data_file)
    return data

def start_loggin():
    '''
    Metodo responsavel por iniciar o log da aplicacao.
    Importante: Ainda em fase de testes. Pois a principio apenas a execucao do
    rest-app.py esta registrando no arquivo.
    :return: 
    '''
    path = get_project_root()
    logging.basicConfig(filename=str(path)+'/locadora.log', level=logging.DEBUG)
    return logging.getLogger()

def criar_banco_de_dados(diretorio, nome_do_banco, excluir_se_existir = False):
    '''
    Metodo responsavel por criar o banco de dados da locadora no padrao
    SQLite
    :param diretorio: Local onde o arquivo do SQLite devera ser gravado
    :param nome_do_banco: Nome do arquivo do SQLite
    :param excluir_se_existir: Permite ao metodo excluir o arquivo se o mesmo
    for licalizado no local indicado
    :return: None
    '''
    try:
        logger = logging.getLogger(__name__)
        logger.debug('Iniciou criar_banco_de_dados')
        #print('os.getcwd() = '+os.getcwd())
        #current_path = os.getcwd() + '/classes/model/database/'

        pode_criar = False

        # Validando a existencia do banco de dados
        if not os.path.exists(diretorio+nome_do_banco):
            print('Banco de dados '+nome_do_banco+' n'+chr(227)+'o localizado')
            pode_criar = True
        else:
            print('Banco de dados '+nome_do_banco+' localizado')
            if excluir_se_existir:
                pode_criar = True
                os.remove(diretorio+nome_do_banco)
        #--------------------------------------------------------


        if pode_criar:

            import sqlite3

            # Criando o banco de dados
            con = sqlite3.connect(diretorio+nome_do_banco)
            cur = con.cursor()

            # Executando a criação das tabelas
            cur.execute(
                'CREATE TABLE carro(' \
                'id integer PRIMARY key AUTOINCREMENT,' \
                'placa varchar(7) not NULL,' \
                'cor varchar(20),' \
                'qtde_portas integer,' \
                'ano_fabricacao integer,' \
                'quilometragem integer,' \
                'valor_diaria float)')

            cur.execute(
                'CREATE TABLE cliente (' \
                'id integer PRIMARY key AUTOINCREMENT,' \
                'nome varchar(60) NOT NULL,' \
                'sexo varchar(1),' \
                'data_nascimento date NOT NULL,' \
                'cnh varchar(20),' \
                'data_vencimento_cnh date,' \
                'endereco varchar(200),' \
                'email varchar(100),' \
                'tel_celular varchar(15) NOT NULL )')

            cur.execute(
                'CREATE table locacao (' \
                'id integer PRIMARY key AUTOINCREMENT,' \
                'id_carro integer not NULL,' \
                'id_cliente INteger not null,' \
                'data_inicial date NOT NULL,' \
                'data_final date,' \
                'km_inicial integer NOT NULL,' \
                'km_final integer,' \
                'valor_total float,' \
                'FOREIGN KEY (id_carro) REFERENCES carro (id) on DELETE RESTRICT,' \
                'FOREIGN key (id_cliente) REFERENCES cliente (id) on DELETE RESTRICT)')

            # fechando a conexão
            con.close()

            print('Banco de dados '+nome_do_banco+' criado com sucesso')
            logger.debug('Banco de dados '+nome_do_banco+' criado com sucesso')

    except Exception as e:
        logger.error('Ocorreu uma falha na cria'+chr(231)+chr(227)+'o do banco de dados: ',e)
        print('Ocorreu uma falha na cria'+chr(231)+chr(227)+'o do banco de dados: ' + str(e))

def iniciar_aplicacao():
    '''
    Metodo responsavel por preparar o banco de dados e do log da aplicacao.
    :return:
    '''
    application_path = get_project_root()
    application_path = str(application_path) + '/'
    data = get_config_data()
    criar_banco_de_dados(application_path + data['diretorio_banco_de_dados'], data['nome_banco_de_dados'], False)
    criar_banco_de_dados(application_path + data['diretorio_banco_de_dados_teste'], data['nome_banco_de_dados_teste'], True)

def placa_valida(placa):
    '''
    Metodo para validar se a placa informada no carro e uma placa que atende aos seguintes padroes:
    AA0000 ou AAA0000 ou AAA0A00
    :param placa em formato texto:
    :return: True or False
    '''
    if len(str(placa)) == 6:
        x = re.search(r"[A-Z]{2}[0-9]{4}", placa)
    else:
        x = re.search(r"[A-Z]{3}[0-9][0-9A-Z][0-9]{2}", placa)
    return x

def cor_valida(cor):
    '''
    Metodo auxiliar para validar se a cor informada e uma cor valida no formato
    hexadecimal
    :param cor: no formato texto
    :return: True ou False
    '''
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', cor)
    return match
