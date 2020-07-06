import data_base
from uteis import usuário
from uteis import validacao
from uteis import layout
from datetime import date


def retirada():
    if validacao.simples(usuário.ur[2]) == True:
        print(usuário.ur[2])


retirada()
