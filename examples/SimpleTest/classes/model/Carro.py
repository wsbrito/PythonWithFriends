class Carro():
    '''
    Classe de negócio que representa o carro
    '''

    _id = -1
    _placa = ''
    _cor = ''
    _qtde_portas = 0
    _ano_fabricacao = 0
    _quilometragem = 0
    _valor_diaria = 0.0

    def getId(self):
        return self._id

    def setId(self,id):
        self._id = id

    def getPlaca(self):
        return self._placa

    def setPlaca(self,placa):
        self._placa = placa

    def getCor(self):
        return self._cor

    def setCor(self,cor):
        self._cor = cor

    def getQtdePortas(self):
        return self._qtde_portas

    def setQtdePortas(self,qtdePortas):
        self._qtde_portas = qtdePortas

    def getAnoFabricacao(self):
        return self._ano_fabricacao

    def setAnoFabricacao(self,anoFabricacao):
        self._ano_fabricacao = anoFabricacao

    def getQuilometragem(self):
        return self._quilometragem

    def setQuilometragem(self,quilometragem):
        self._quilometragem = quilometragem

    def getValorDiaria(self):
        return self._valor_diaria

    def setValorDiaria(self,valorDiaria):
        self._valor_diaria = valorDiaria

    def validar(self):
        '''
        Método responsável pela validação dos dados. Se o que foi preenchido está em conforme
        com a obrigatoriedade e tipo de dado
        :return: Dicionário com os erros encontrados
        '''
        retorno = {}

        if(len(str(self._placa)) == 0):
            retorno['placa'] = 'Placa é de preenchimento obrigatório'

        try:
            int(self._ano_fabricacao)
        except:
            retorno['ano_fabricacao'] = 'Ano de fabricação é um dado numérico'

        try:
            int(self._qtde_portas)
        except:
            retorno['qtde_portas'] = 'A quantidade de portas é um dado numérico'

        try:
            int(self._quilometragem)
        except:
            retorno['quilometragem'] = 'A quilometragem é um dado numérico'

        try:
            float(self._valor_diaria)
        except:
            retorno['valor_diaria'] = 'O valor da diária é um dado numérico'

        return retorno
    # validar
    #-------------------------------------------------------------------------------------

    def __str__(self):
        '''
        Método auxiliar para a impressão do objeto carro
        :return:
        '''
        return "Placa: "+str(self._placa)+"\n"+\
            "Ano fabricação: "+str(self._ano_fabricacao)+"\n"+\
            "Quilometragem: "+str(self._quilometragem)+"\n"+\
            "Cor: "+str(self._cor)+"\n"+\
            "Qtde. portas: "+str(self._qtde_portas)+"\n"+\
            "Valor diária: "+str(self._valor_diaria)
    #-------------------------------------------------------------------------------------
