'''
Start poin of Python With Friends application.
'''
from classes.model import Carro
from classes.model.database import CarroDB

c = Carro.Carro()

c.setPlaca('KXB1420')

c.setCor('Azul')

c.setQtdePortas(4)

c.setAnoFabricacao(2000)

c.setQuilometragem(1000)

c.setValorDiaria(85.9)

carroDB = CarroDB.CarroDB()

carroDB.inserir(c)
