from uteis import validacao
from uteis import layout


def cadastro_cliente():
    layout.layout('CADASTRO de CLIENTES')
    n = str(input('Cliente: ')).strip().upper()
    s = str(input('Sexo [M\F]: ')).strip().upper()
    ano_nascimento = int(input('Ano de Nascimento: '))
    return ano_nascimento


def modelo_carro():
    layout.layout('Escolha o modelo do carro')
    print('''== \033[33mOpções de potência de motor\033[m ==
       \33[34m[1]        Motor 1.0\033[m  \33[32mR$50\33[m
       \33[34m[2]        Motor 2.0\033[m  \33[32mR$60\33[m                                         
       \33[34m[3]        Motor V12\033[m  \33[32mR$100\33[m''')
    mc = int(input('Qual a sua opção? '))
    return mc


def retirada_user_view():
    loc = ('Dia de Locação: ', 'Mês de Locação: ', 'Ano da Locação: ')
    lista_dias_ret = []
    layout.layout('\33[36mRetirada\033[m')
    for data_ret in loc:
        user = (int(input(f'{data_ret}')))
        lista_dias_ret.append(user)
    return lista_dias_ret


def dev_user_view():
    dev = ('Dia da Devolução: ', 'Mês da Devolução: ', 'Ano da Devolução: ')
    lista_dias_dev = []
    layout.layout('\33[36mDevolução\033[m')
    for data_dev in dev:
        user_dev = (int(input(f'{data_dev}')))
        lista_dias_dev.append(user_dev)
    return lista_dias_dev


mc = modelo_carro()
a = retirada_user_view()
b = dev_user_view()



