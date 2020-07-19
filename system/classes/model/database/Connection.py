'''
Classe responsável pela conexão com a base de dados
'''
import sqlite3
import os

class Connection():
    '''

    '''

    def getConnection(self):
        '''

        :return: Objeto connect do SQLite
        '''
        current_path = os.getcwd() + '/classes/model/database/'
        print(current_path)
        return sqlite3.connect(current_path + 'locadora.db')

    def getCursos(self):
        '''

        :return: Objeto cursor do SQLite
        '''
        return self.getConnection().cursor()