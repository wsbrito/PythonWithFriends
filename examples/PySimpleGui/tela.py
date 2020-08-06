import PySimpleGUI as sg

class TelaPython():

    def __init__(self):
        sg.ChangeLookAndFeel('SystemDefault')
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais serviços de e-mail são aceitos?')],
            [sg.Checkbox('GMail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,15),visible=True,key='output')]
        ]

        # Janela
        self.janela = sg.Window('Dados do usuário').layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            print(self.values)
            '''
            É possível recuperar os dados através das chaves
            '''
            nome = self.values['nome']
            print(f'nome: {nome}')

tela = TelaPython()

tela.Iniciar()