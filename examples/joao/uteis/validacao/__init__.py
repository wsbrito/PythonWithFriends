from datetime import date
from uteis import usuário


def vcc(ano_nascimento):       # validação cadastro cliente
    '''
    :param ano_nascimento: Recebe do def cadastro_cliente a váriável ano_nascimento
    :return: a idade atual do cliente
    '''
    idade_atual = date.today().year - ano_nascimento
    while 18 >= idade_atual <= 85:
        print('\33[32mLocação indisponível por razão de idade\33[m')
        break
    else:
        return idade_atual


def vmc(mc):   # validação modelo carro
    '''
    :param mc: Recebe a def modelo_carro
    :return: Falso caso a opção digitada não esteja dentro da lista de opções
    '''
    while True:
        if mc in [1, 2, 3]:
            break
        else:
            print('Escolha um modelo válido.')
            return False


def simples(loc):   # Simplificando a Operação
    '''
    :param loc: ano da locação
    :param n1: ano referência para o limite de locação: 2022
    :param n2: ano atual
    :return: True caso o ano da locação não seja maior que 2022 e\ou menor que o ano corrente
    '''
    while True:
         if loc > 2022 or loc < date.today().year:
             print('Escreva uma opção válida.')
             break
         else:
             return True


'''def r():
    if 18 <= usuário.cadastro_cliente() <= 85:
        usuário.modelo_carro()
    else:
        print('Fim')'''


#r()




