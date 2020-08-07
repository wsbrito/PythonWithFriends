'''
Arquivo da classe Connection
'''
import sqlite3
import os

class Connection(object):
    '''
    Classe responsavel pela conexao com a base de dados
    '''

    @classmethod
    def get_connection(cls):
        '''
        Metodo para retornar uma conexao com o banco de dados locadora.db.
        :return: Objeto connect do SQLite
        '''
        current_path = os.getcwd() + '/classes/model/database/'
        #print(current_path)
        return sqlite3.connect(current_path + 'locadora.db')
    #--------------------------------------------------------------------

    def get_cursor(self):
        '''
        Metodo para retornar um objeto cursor
        :return: Objeto cursor do SQLite
        '''
        return self.get_connection().cursor()
    #--------------------------------------------------------------------
