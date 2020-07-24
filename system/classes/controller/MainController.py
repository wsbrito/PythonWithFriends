import classes.view.CarroView as cv
import classes.controller.CarroController as cc

class MainController():
    '''
    Classe responsável por coordenar os principais fluxos das funcionalidades do sistema
    como também se encarregará de cuidar da locação e devolução
    '''

    def opcaoCadastrarCarro(self):
        '''
        Método que irá instaciar um objeto da classe CarroView para
        a apresentação da tela para cadastro do carro
        :return:
        '''
        carroView = cv.CarroView()
        carroView.opcaoCadastrarCarro()
    #-----------------------------------------------------------------------

    def opcaoAlterarCarro(self):
        '''
        Metodo responsavel pela apresentaçao de lista de carros na tela
        :return:
        '''
        carroController = cc.CarroController()
        carroController.listar()
    #-----------------------------------------------------------------------
