from classes.model import Carro
from classes.model.database import Connection

class CarroDB(Connection.Connection):

    def inserir(self,carro):
        '''

        :return:
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
