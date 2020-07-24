'''
Start poin of Python With Friends application.
'''
import classes.view.MenuPrincipalView as menu

def main():
    '''
    Definição do método main que será responsável por instanciar a classe
    MenuPrincipalVeiw
    '''
    # Instanciando um objeto da MenuPrincipalView
    telaInicial = menu.MenuPrincipalView()
    encerrou = telaInicial.opcoesSistema()
    while(not encerrou):
        encerrou = telaInicial.opcoesSistema()
    print("Fim do programa")
#------------------------------------------------------------------------

if __name__ == '__main__':
    '''
    Execução do método main
    '''
    main()