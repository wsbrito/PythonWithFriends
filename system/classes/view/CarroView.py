'''
Arquivo da classe CarroView
'''
from classes.view import MainView
import classes.model.Carro as c
import classes.controller.CarroController as cc

class CarroView(MainView.MainView):
    '''
    Classe responsavel pelas telas para manutecao do carro no sistema
    '''

    def opcao_cadastrar_carro(self):
        '''
        Metodo responsavel por capturar os dados para o cadastro do carro
        '''
        try:
            self.limparTela()
            dadosCarro = {
                'placa':'Informe a placa do ve'+chr(237)+'culo',
                'cor':'Informe a cor do ve'+chr(237)+'culo',
                'qtde_portas':'Informe a quantidade de portas do ve'+chr(237)+'culo',
                'ano_fabricacao':'Informe o ano de fabrica'+chr(231)+chr(227)+'o do ve'+chr(237)+'culo',
                'quilometragem':'Informe a quilometragem do ve'+chr(237)+'culo',
                'valor_diaria':'Informe o valor da di'+chr(225)+'ria'
            }
            dadosLidos = self.recuperarDados(dadosCarro)
            novoCarro = c.Carro()
            self.__atribuirDadosLidosTela(novoCarro,dadosLidos)

            # Enquanto os dados nao forem validos
            dadosNaoValidados = novoCarro.validar()
            while( len(dadosNaoValidados) > 0):
                self.limparTela()
                self.__apresentar_erros(dadosNaoValidados)
                print("Favor informar novamente os seguintes dados")
                dadosParaLeitura = \
                    self.__organizarDadosLeitura(dadosCarro,dadosNaoValidados)
                dadosLidos = self.recuperarDados(dadosParaLeitura)
                self.__atribuirDadosLidosTela(novoCarro, dadosLidos)
                dadosNaoValidados = novoCarro.validar()
            #-----------------------------------------------------------------------------

            #Confirmar com o usuario a inclusao do carro
            print(novoCarro)
            confirma = input("Confirma a inclus"+chr(277)+"o do carro?[S/N] ")
            if('s' in str(confirma).lower()):
                carroController = cc.CarroController()
                carroController.incluir(novoCarro)
                print("Carro inclu"+chr(237)+"do com sucesso.")
            else:
                print("Opera"+chr(231)+chr(227)+"o cancelada")
        except Exception as e:
            print("Ocorreu uma falha na inclus"+chr(227)+"o do carro "+ str(e))
    #--------------------------------------------------------------------------------

    def __organizarDadosLeitura(self, dados_lidos, dados_nao_validados):
        '''
        Metodo auxiliar para criar um dicionario com apenas os dados que nao
        foram validados
        :param dadosLidos:
        :param dadosNaoValidados:
        :return:
        '''
        retorno = {}
        for d, v in dados_nao_validados.items():
            retorno[d] = dados_lidos[d]
        return retorno
    #--------------------------------------------------------------------------------

    def __atribuirDadosLidosTela(self, carro, dados_lidos):
        '''
        Metodo auxiliar para atribuir os dados lidos ao objeto carro
        :param carro:
        :param dadosLidos:
        :return:
        '''
        if 'cor' in dados_lidos:
            carro.set_cor(dados_lidos['cor'])
        if 'placa' in dados_lidos:
            carro.set_placa(dados_lidos['placa'])
        if 'qtde_portas' in dados_lidos:
            carro.set_qtde_portas(dados_lidos['qtde_portas'])
        if 'valor_diaria' in dados_lidos:
            carro.set_valor_diaria(dados_lidos['valor_diaria'])
        if 'ano_fabricacao' in dados_lidos:
            carro.set_ano_fabricacao(dados_lidos['ano_fabricacao'])
        if 'quilometragem' in dados_lidos:
            carro.set_quilometragem(dados_lidos['quilometragem'])
    #--------------------------------------------------------------------------------

    def apresentarListaCarro(self, lista_carro):
        '''
        Metodo responsavel por apresentar a lista de carros em tela
        :param listaCarro:
        '''
        self.limparTela()
        print("Lista de carros\n")
        print("PLACA\tANO\tKM\tCOR\tQTDE PORTAS\tDI"+chr(193)+"RIA")
        for carro in lista_carro:
            print(str(carro.get_placa())+"\t"+\
                  str(carro.get_ano_fabricacao())+"\t"+\
                  str(carro.get_quilometragem())+"\t"+\
                  str(carro.get_cor())+"\t"+\
                  str(carro.get_qtde_portas())+"\t\t"+\
                  str(carro.get_valor_diaria()))
    #--------------------------------------------------------------------------------

    def __apresentar_erros(self, erros):
        '''
        Metodo para exibicao dos erros de validacao encotrados em tela
        :param erros Dicionario com os erro:
        '''
        print("Os seguintes problemas foram identificados:")
        for erro in erros.values():
            print(erro)
    #--------------------------------------------------------------------------------
