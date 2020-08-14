import PySimpleGUI as sg

class MainMenu(object):

    def __init__(self):

        # Aparência
        sg.ChangeLookAndFeel('SystemDefault')

        # Layout - Campos para serem exibidos
        menu_def = [['&Clientes', ['&Inclusão', '&Alteração']],
                    ['&Veículos', ['I&nclusão', 'A&lteração']],
                    ['&Locação',  ['&Registrar', '&Devolução']],
                    ['A&juda', '&Sobre...'], ]

        option1 = sg.Button("Option 1",enable_events=True)

        opcoes = [
            option1,
            sg.Button("Option 2"),
            sg.Button("Option 3"),
            sg.Button("Option 4"),
        ]

        rodape = [sg.Text('Rodape')]


        layout = [
            #[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]
            [sg.Menu(menu_def, tearoff=True)],
            opcoes,
            rodape
        ]

        # Janela
        self.janela = sg.Window('Menu principal',size=(800,600)).layout(layout)

    def show_screen(self):
        while True:
            event, values = self.janela.read()

            # End program if user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                break

        self.janela.close()
