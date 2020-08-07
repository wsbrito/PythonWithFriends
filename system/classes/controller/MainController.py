'''
Arquivo referente a classe MainController
'''
import classes.view.CarroView as cv
import classes.controller.CarroController as cc

class MainController(object):
    '''
    Classe responsavel por coordenar os principais fluxos das funcionalidades do sistema
    como tambem se encarregara de cuidar da locacao e devolucao
    '''

    @classmethod
    def opcao_cadastrar_carro(cls):
        '''
        Metodo que ira instaciar um objeto da classe CarroView para
        a apresentacao da tela para cadastro do carro
        '''
        carro_view = cv.CarroView()
        carro_view.opcaoCadastrarCarro()
    #-----------------------------------------------------------------------

    @classmethod
    def opcao_alterar_carro(cls):
        '''
        Metodo responsavel pela apresentacao de lista de carros na tela
        '''
        carro_controller = cc.CarroController()
        carro_controller.listar()
    #-----------------------------------------------------------------------
