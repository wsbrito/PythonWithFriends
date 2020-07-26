from classes.model import Carro
from classes.model.database import Connection

class CarroDB(Connection.Connection):
    '''
    Classe responsável pelos acessos a tabela carro
    '''

    def inserir(self,carro):
        '''
        Método responsável pela inclusão do carro na base de dados.
        '''
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO carro (placa,cor,qtde_portas,ano_fabricacao,quilometragem,valor_diaria)' \
                ' VALUES (?,?,?,?,?,?)',
                (carro.getPlaca(),
                 carro.getCor(),
                 carro.getQtdePortas(),
                 carro.getAnoFabricacao(),
                 carro.getQuilometragem(),
                 carro.getValorDiaria()))

            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print('Ocorreu uma falha na inclusão do carro: ' + str(e))
    #----------------------------------------------------------------------------------------

    def listar(self):
        '''
        Método responsável pela recuperação de todos os carros da base de dados
        :return: Lista de objetos carros
        '''
        retorno = []
        try:
            connection = self.getConnection()
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
                carro.setId(linha[0])
                carro.setPlaca(linha[1])
                carro.setCor(linha[2])
                carro.setQtdePortas(linha[3])
                carro.setAnoFabricacao(linha[4])
                carro.setQuilometragem(linha[5])
                carro.setValorDiaria(linha[6])
                retorno.append(carro)
        except Exception as e:
            print('Ocorreu uma falha na listagem dos carros: ' + str(e))
        return retorno
    #----------------------------------------------------------------------------------------

    def alterar(self,carro):
        '''
        Método responsável pelo atualização do objeto Carro na base de dados
        :param carro:
        :return:
        '''
    #----------------------------------------------------------------------------------------

    def excluir(self,carro):
        '''
        Método responsável pela exclusão do Carro na base de dados.
        :param carro:
        :return:
        '''
    # ----------------------------------------------------------------------------------------

