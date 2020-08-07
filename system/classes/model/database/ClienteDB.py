'''
Arquivo da classe ClienteDB
'''
#from classes.model.Cliente import Cliente

class ClienteDB(object):
    '''
    Classe responsavel pela manipulacao dos dados do cliente na base de dados
    '''

    def inserir(self, cliente):
        '''
        Metodo responsavel pela inclusao do objeto Cliente na base de dados
        :param cliente:
        '''
    # ----------------------------------------------------------------------------------------

    def alterar(self, cliente):
        '''
        Metodo responsavel pelo atualizacao do objeto Cliente na base de dados
        :param cliente
        '''
    # ----------------------------------------------------------------------------------------

    def excluir(self, cliente):
        '''
        Metodo responsavel pela exclusao do Cliente na base de dados.
        :param cliente
        '''
    # ----------------------------------------------------------------------------------------

    # esse decorator deve ser retirado quando o metodo for conluido
    @classmethod
    def listar(cls):
        '''
        Metodo para retornar a lista de clientes
        :return: List de Cliente
        '''
        return []
