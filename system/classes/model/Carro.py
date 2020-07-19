class Carro():
    '''

    '''
    _placa = ''
    _cor = ''
    _qtde_portas = 0
    _ano_fabricacao = 0
    _quilometragem = 0
    _valor_diaria = 0.0

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
