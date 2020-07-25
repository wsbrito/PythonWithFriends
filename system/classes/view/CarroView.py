import classes.view.MainView as mv
import classes.model.Carro as c
import classes.controller.CarroController as cc

class CarroView(mv.MainView):
    '''
    Classe responsável pelas telas para manuteção do carro no sistema
    '''

    def opcaoCadastrarCarro(self):
        '''
        Método responsável por capturar os dados para o cadastro do carro
        :return:
        '''
        try:
            self.limparTela()
            dadosCarro = {
                'placa':'Informe a placa do veículo',
                'cor':'Informe a cor do veículo',
                'qtde_portas':'Informe a quantidade de portas do veículo',
                'ano_fabricacao':'Informe o ano de fabricação do veículo',
                'quilometragem':'Informe a quilometragem do veículo',
                'valor_diaria':'Informe o valor da diária'
            }
            dadosLidos = self.recuperarDados(dadosCarro)
            novoCarro = c.Carro()
            self.__atribuirDadosLidosTela(novoCarro,dadosLidos)

            # Enquanto os dados não forem válidos
            dadosNaoValidados = novoCarro.validar()
            while( len(dadosNaoValidados) > 0):
                self.limparTela()
                self.__apresentarErros(dadosNaoValidados)
                print("Favor informar novamente os seguintes dados")
                dadosParaLeitura = \
                    self.__organizarDadosLeitura(dadosCarro,dadosNaoValidados)
                dadosLidos = self.recuperarDados(dadosParaLeitura)
                self.__atribuirDadosLidosTela(novoCarro, dadosLidos)
                dadosNaoValidados = novoCarro.validar()
            #-----------------------------------------------------------------------------

            #Confirmar com o usuário a inclusão do carro
            print(novoCarro)
            confirma = input("Confirma a inclusão do carro?[S/N] ")
            if('s' in str(confirma).lower()):
                carroController = cc.CarroController()
                carroController.incluir(novoCarro)
                print("Carro incluído com sucesso.")
            else:
                print("Operação cancelada")
        except Exception as e:
            print("Ocorreu uma falha na inclusão do carro "+ str(e))
    #--------------------------------------------------------------------------------

    def __organizarDadosLeitura(self,dadosLidos,dadosNaoValidados):
        '''
        Método auxiliar para criar um dicionário com apenas os dados que não
        foram validados
        :param dadosLidos:
        :param dadosNaoValidados:
        :return:
        '''
        retorno = {}
        for d, v in dadosNaoValidados.items():
            retorno[d] = dadosLidos[d]
        return retorno
    #--------------------------------------------------------------------------------

    def __atribuirDadosLidosTela(self,carro,dadosLidos):
        '''
        Método auxiliar para atribuir os dados lidos ao objeto carro
        :param carro:
        :param dadosLidos:
        :return:
        '''
        if 'cor' in dadosLidos:
            carro.setCor(dadosLidos['cor'])
        if 'placa' in dadosLidos:
            carro.setPlaca(dadosLidos['placa'])
        if 'qtde_portas' in dadosLidos:
            carro.setQtdePortas(dadosLidos['qtde_portas'])
        if 'valor_diaria' in dadosLidos:
            carro.setValorDiaria(dadosLidos['valor_diaria'])
        if 'ano_fabricacao' in dadosLidos:
            carro.setAnoFabricacao(dadosLidos['ano_fabricacao'])
        if 'quilometragem' in dadosLidos:
            carro.setQuilometragem(dadosLidos['quilometragem'])
    #--------------------------------------------------------------------------------

    def apresentarListaCarro(self,listaCarro):
        '''
        Método responsável por apresentar a lista de carros em tela
        :param listaCarro:
        :return:
        '''
        self.limparTela()
        print("Lista de carros\n")
        print("PLACA\tANO\tKM\tCOR\tQTDE PORTAS\tDIÁRIA")
        for carro in listaCarro:
            print(str(carro.getPlaca())+"\t"+\
                  str(carro.getAnoFabricacao())+"\t"+\
                  str(carro.getQuilometragem())+"\t"+\
                  str(carro.getCor())+"\t"+\
                  str(carro.getQtdePortas())+"\t\t"+\
                  str(carro.getValorDiaria()))
    #--------------------------------------------------------------------------------

    def __apresentarErros(self,erros):
        '''
        Método para exibição dos erros de validação encotrados em tela
        :param erros Dicionário com os erro:
        :return:
        '''
        print("Os seguintes problemas foram identificados:")
        for erro in erros.values():
            print(erro)
    #--------------------------------------------------------------------------------
