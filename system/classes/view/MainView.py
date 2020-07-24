from os import system, name

class MainView():
    '''
    Classe que servirá de bases para as demais classes view.
    Criada, a princípio, para o reproveitamento do métoodo de limpeza da tela
    '''

    def limparTela(self):
        '''
        Método auxiliar para limpeza da tela
        '''
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def recuperarDados(self,dados):
        '''
        Método que recebe um dicionário com as mensagens que apresentará em tela e retornará
        para cada chave o dado informado pelo usuário
        :param dados: dicionário com os dados desejados
        :return: dicionário com os dados informados pelo usuário
        '''
        retorno = {}
        for atributo, mensagem in dados.items():
            dadoLido = input(mensagem+" ")
            retorno[atributo] = dadoLido
        return retorno