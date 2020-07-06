import data_base
from uteis import usuário
from uteis import validacao
from uteis import layout
from datetime import date


def retirada():
   if validacao.simples(usuário.a[2]) == True:
       return usuário.a[0]


def devolucao():
    if validacao.simples(usuário.b[2]) == True:
        return usuário.b[0]


def permanencia():
    per = devolucao() - retirada()
    return per


def calculo_locacao():
    cl = usuário.mc
    print(len(cl))


calculo_locacao()



