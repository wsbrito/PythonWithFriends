'''
Arquivo da classe CarroDB
'''
from __future__ import print_function
import logging
import sqlite3
from classes.model import Carro
from classes.model.database import Connection

class CarroDB(Connection.Connection):
    '''
    Classe responsavel pelos acessos a tabela carro
    '''

    def inserir(self, carro):
        '''
        Metodo responsavel pela inclusao do carro na base de dados.
        :return Dicionario com { 'id':'Id do carro inserido', 'msg':'Carro inserido com sucesso' } ou
        { 'erro':'Mensagem de erro no processo' }
        '''
        try:
            logging.debug('Iniciou o inserir carro')
            connection = self.get_connection()
            cursor = connection.cursor()
            # Inserindo o registo do carro
            cursor.execute(
                'INSERT INTO carro (placa,cor,qtde_portas,'\
                'ano_fabricacao,quilometragem,valor_diaria)' \
                ' VALUES (?,?,?,?,?,?)',
                (carro.get_placa(),
                 carro.get_cor(),
                 carro.get_qtde_portas(),
                 carro.get_ano_fabricacao(),
                 carro.get_quilometragem(),
                 carro.get_valor_diaria()))
            # Recuperando o ID inderido
            cursor.execute('SELECT last_insert_rowid()');
            for id in cursor.fetchall():
                retorno = dict([('id',id[0]),('msg','Carro inserido com sucesso')])
            connection.commit()
            cursor.close()
            connection.close()
            logging.debug('Carro inserido com sucesso')
            return retorno
        except sqlite3.DatabaseError as db_erro:
            logging.error('Ocorreu uma falha na inclusão do carro',db_erro)
            print('Ocorreu uma falha na inclusão do carro: ' + str(db_erro))
            return dict([('erro',str(db_erro))])
    #----------------------------------------------------------------------------------------

    def listar(self):
        '''
        Metodo responsavel pela recuperacao de todos os carros da base de dados
        :return: Lista de objetos carros
        '''
        retorno = []
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                'SELECT '\
                '   id '\
                '   ,placa'\
                '   ,cor'\
                '   ,qtde_portas'\
                '   ,ano_fabricacao'\
                '   ,quilometragem'\
                '   ,valor_diaria '\
                'FROM carro ')
            for linha in cursor.fetchall():
                carro = Carro.Carro()
                carro.set_id(linha[0])
                carro.set_placa(linha[1])
                carro.set_cor(linha[2])
                carro.set_qtde_portas(linha[3])
                carro.set_ano_fabricacao(linha[4])
                carro.set_quilometragem(linha[5])
                carro.set_valor_diaria(linha[6])
                retorno.append(carro)
        except sqlite3.DatabaseError as db_erro:
            print('Ocorreu uma falha na listagem dos carros: ' + str(db_erro))
        return retorno
    #----------------------------------------------------------------------------------------

    def alterar(self, carro):
        '''
        Metodo responsavel pelo atualizacao do objeto Carro na base de dados
        :param carro:
        :return:
        '''
    #----------------------------------------------------------------------------------------

    def excluir(self, carro):
        '''
        Metodo responsavel pela exclusao do Carro na base de dados.
        :param carro:
        :return:
        '''
    # ----------------------------------------------------------------------------------------

