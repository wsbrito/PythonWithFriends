import sqlite3
import os

class Connection():
    '''
    Classe responsável pela conexão com a base de dados
    '''

    def getConnection(self):
        '''
        Método para retornar uma conexão com o banco de dados locadora.db.
        :return: Objeto connect do SQLite
        '''
        current_path = os.getcwd() + '/classes/model/database/'
        print(current_path)
        return sqlite3.connect(current_path + 'locadora.db')

    def getCursos(self):
        '''
        Método para retornar um objeto cursor
        :return: Objeto cursor do SQLite
        '''
        return self.getConnection().cursor()