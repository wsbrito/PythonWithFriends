'''
Arquivo da classe TestePylint
'''
from __future__ import print_function

class TestePylint(object):
    '''
    Classe TestePylint
    '''
    __mensagem_padrao = 'Mensagem padr'+chr(277)+'o.'

    def exibir_mensagem(self, texto):
        '''
        Metodo exibir mensagem
        :param texto:
        '''
        if len(texto) != 0:
            print(texto)
        else:
            print(self.__mensagem_padrao)

    @classmethod
    def realizar_soma(cls, num1, num2):
        '''
        Metodo para somar dois numeros
        :param num1:
        :param num2:
        :return: soma do num1 com o num2
        '''
        return num1 + num2
