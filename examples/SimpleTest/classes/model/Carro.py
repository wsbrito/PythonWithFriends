'''
Carro.py - arquivo da classe Carro
'''
class Carro(object):
    '''
    Classe de negocio que representa o carro
    '''

    _id = -1
    _placa = ''
    _cor = ''
    _qtde_portas = 0
    _ano_fabricacao = 0
    _quilometragem = 0
    _valor_diaria = 0.0

    def get_id(self):
        '''
        metodo getter para o id do carro
        :return: id do carro
        '''
        return self._id

    def set_id(self, _id):
        '''
        metodo setter para o id do carro
        '''
        self._id = _id

    def get_placa(self):
        '''
        metodo getter para a placa do carro
        :return: placa do carro
        '''
        return self._placa

    def set_placa(self, placa):
        '''
        metodo setter para a placa do carro
        '''
        self._placa = placa

    def get_cor(self):
        '''
        metodo getter para a placa do carro
        :return: cor do carro
        '''
        return self._cor

    def set_cor(self, cor):
        '''
        metodo setter para a cor do carro
        '''
        self._cor = cor

    def get_qtde_portas(self):
        '''
        metodo getter para a quantidade de portas do carro
        :return: cor do carro
        '''
        return self._qtde_portas

    def set_qtde_portas(self, qtde_portas):
        '''
        metodo setter para a quantidade de portas do carro
        '''
        self._qtde_portas = qtde_portas

    def get_ano_fabricacao(self):
        '''
        metodo getter para o ano de fabricacao do carro
        :return: cor do carro
        '''
        return self._ano_fabricacao

    def set_ano_fabricacao(self, ano_fabricacao):
        '''
        metodo setter para o ano de fabricacao do carro
        '''
        self._ano_fabricacao = ano_fabricacao

    def get_quilometragem(self):
        '''
        metodo getter para kilometragem do carro
        :return: cor do carro
        '''
        return self._quilometragem

    def set_quilometragem(self, quilometragem):
        '''
        metodo setter para kilometragem do carro
        '''
        self._quilometragem = quilometragem

    def get_valor_diaria(self):
        '''
        metodo getter para o valor da diaria do carro
        :return: cor do carro
        '''
        return self._valor_diaria

    def set_valor_diaria(self, valor_diaria):
        '''
        metodo setter para o valor da diaria do carro
        '''
        self._valor_diaria = valor_diaria

    def validar(self):
        '''
        Metodo responsavel pela validacao dos dados. Se o que foi preenchido esta em conforme
        com a obrigatoriedade e tipo de dado
        :return: Dicionario com os erros encontrados
        '''
        retorno = {}

        if len(str(self._placa)) == 0:
            retorno['placa'] = 'Placa '+chr(233)+' de preenchimento obrigat'+chr(243)+'rio'

        try:
            int(self._ano_fabricacao)
        except ValueError:
            retorno['ano_fabricacao'] = \
                'Ano de fabrica'+chr(231)+chr(277)+'o '+chr(233)+' um dado num'+chr(233)+'rico'

        try:
            int(self._qtde_portas)
        except ValueError:
            retorno['qtde_portas'] = 'A quantidade de portas '\
                                     +chr(233)+' um dado num'+chr(233)+'rico'

        try:
            int(self._quilometragem)
        except ValueError:
            retorno['quilometragem'] = 'A quilometragem '+chr(233)+' um dado num'+chr(233)+'rico'

        try:
            float(self._valor_diaria)
        except ValueError:
            retorno['valor_diaria'] = \
                'O valor da di'+chr(225)+'ria '+chr(233)+' um dado num'+chr(233)+'rico'

        return retorno
    # validar
    #-------------------------------------------------------------------------------------

    def __str__(self):
        '''
        Metodo auxiliar para a impressao do objeto carro
        :return:
        '''
        return "Placa: "+str(self._placa)+"\n"+\
            "Ano fabrica"+chr(231)+chr(277)+"o: "+str(self._ano_fabricacao)+"\n"+\
            "Quilometragem: "+str(self._quilometragem)+"\n"+\
            "Cor: "+str(self._cor)+"\n"+\
            "Qtde. portas: "+str(self._qtde_portas)+"\n"+\
            "Valor di"+chr(225)+"ria: "+str(self._valor_diaria)
    #-------------------------------------------------------------------------------------
