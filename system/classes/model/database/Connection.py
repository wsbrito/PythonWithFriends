'''
Arquivo da classe Connection
'''
import sqlite3
import json

class Connection(object):
    '''
    Classe responsavel pela conexao com a base de dados
    '''

    def __init__(self, banco_de_teste = False):
        self._banco_de_teste = banco_de_teste

    def get_connection(self):
        '''
        Metodo para retornar uma conexao com o banco de dados locadora.db.
        :return: Objeto connect do SQLite
        '''

        '''
        Essa forcacao do caminho do arquivo nao ficou legal mas teremos que
        conviver com ela ate conseguirmos uma solucao definitiva
        '''
        with open("../../../config.json") as json_data_file:
            data = json.load(json_data_file)

        if self._banco_de_teste:
            return sqlite3.connect('../../../'+data['diretorio_banco_de_dados_teste'] + data['nome_banco_de_dados_teste'])

        return sqlite3.connect(data['diretorio_banco_de_dados'] + data['nome_banco_de_dados'])
    #--------------------------------------------------------------------

    def get_cursor(self):
        '''
        Metodo para retornar um objeto cursor
        :return: Objeto cursor do SQLite
        '''
        return self.get_connection().cursor()
    #--------------------------------------------------------------------
