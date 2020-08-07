'''
Arquivo referente a classe Cliente
'''
class Cliente(object):
    '''
    Classe de negocio relacionada ao cliente da locadora
    '''

    # Definicao dos atributos

    # Metodos get e set (acessores) para cada atributo

    # esse decorator devera ser retirado quando a classe estiver pronta
    @classmethod
    def validar(cls):
        '''
        Metodo para validacao do objeto antes de sua percistencia na base de dados
        :return: Dicionario com os atributos e falhas encontradas
        '''
        return {}
