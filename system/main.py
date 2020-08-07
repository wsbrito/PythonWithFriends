'''
Start poin of Python With Friends application.
'''
from __future__ import print_function
import classes.view.MenuPrincipalView as menu

def main():
    '''
    Definicao do metodo main que sera responsavel por instanciar a classe
    MenuPrincipalVeiw
    '''
    tela_inicial = menu.MenuPrincipalView()
    encerrou = tela_inicial.opcoes_sistema()
    while not encerrou:
        encerrou = tela_inicial.opcoes_sistema()
    print("Fim do programa")
    #------------------------------------------------------------------------

if __name__ == '__main__':
    #Execucao do metodo main
    main()
