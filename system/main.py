'''
Start poin of Python With Friends application.
'''
import classes.view.MenuPrincipalView as menu

'''
Definição do método main que será responsável por instanciar a classe 
MenuPrincipalVeiw
'''
def main():
    # Instanciando um objeto da MenuPrincipalView
    telaInicial = menu.MenuPrincipalView()
    encerrou = telaInicial.opcoesSistema()
    while(not encerrou):
        encerrou = telaInicial.opcoesSistema()
    print("Fim do programa")
#------------------------------------------------------------------------

'''
Execução do método main
'''
if __name__ == '__main__':
    main()