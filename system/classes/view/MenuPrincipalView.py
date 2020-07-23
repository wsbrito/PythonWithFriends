'''
Classe responsável pelas iterações iniciais da aplicação com o usuário e
da chamada as demais classes da camada de apresentações do sistema
'''
from os import system, name

class MenuPrincipalView():

    '''
    Variável para controle do encerramento do sistema
    '''
    _encerrar_programa = False

    '''
    Lista das opções do programa
    '''
    _opcoes = [0,1,2,3,4,5,6]

    '''
    Mètodo auxiliar para apresentar as opções na tela
    '''
    def imprimeOpcoes(self):
        print("PYTHON WITH FRIEDNS - Locadora system\n\n")
        print("Opçoes do sistema:")
        print("1 - Cadastro de carro\n")
        print("2 - Atualizar carro\n")
        print("3 - Cadastro de cliente\n")
        print("4 - Atualizar cliente\n")
        print("5 - Registrar locação\n")
        print("6 - Registrar devolução\n\n")
        print("0 - Encerrar o programa")


    '''
    Tela inicial da aplicação com as principais operações do sistema
    '''
    def opcoesSistema(self):
        self.limparTela()
        self.imprimeOpcoes()
        tecla = input("\nInforme a opção desejada e pressione a tecla ENTER para confirmar: ")
        self.validarOpcaoInformada(tecla)
        return self._encerrar_programa

    '''
    Método para verificar se o que foi informado pelo usuário é uma opção válida e retonar 
    '''
    def validarOpcaoInformada(self,tecla):
        try:
            opcao = int(tecla)
            if(opcao in self._opcoes):
                '''
                Se a opção selecionada for 0 interrompe a execução do método
                '''
                if(opcao == 0):
                    self._encerrar_programa = True
                    return
                if(opcao == 1):
                    print("Cadastrar carro >> A opções ainda não está disponível")
                elif(opcao == 2):
                    print("Atualizar carro >> A opções ainda não está disponível")
                elif(opcao == 3):
                    print("Cadastro de cliente >> A opções ainda não está disponível")
                elif(opcao == 4):
                    print("Atualizar de cliente >> A opções ainda não está disponível")
                elif (opcao == 5):
                    print("5 - \n")
                    print("Registrar locação >> A opções ainda não está disponível")
                elif (opcao == 6):
                    print("Registrar devolução >> A opções ainda não está disponível")
                input("\nPressione a teclar ENTER para continuar")
            else:
                print("Opção inválida")
                self.opcoesSistema()
        except Exception as e:
            print("Não foi possível identificar a opções selecionada. Tente novamente")
            self.opcoesSistema()
    '''
    Método auxiliar para limpeza da tela
    '''
    def limparTela(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')