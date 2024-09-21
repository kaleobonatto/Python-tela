import PySimpleGUI as sg

sg.theme('Dark Blue 3')


layout_principal = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher Pasta Anexos',target='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta Planilha',target='input_planilha'),sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Principal',layout=layout_principal)


while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        anexos = values['input_anexos']
        anexos2 = values['input_planilha']
        print(f'O Email foi:{email}')
        print(f'a senha foi:{senha}')
        print(f'O anexo foi:{anexos}')
        print(f'A planilha foi:{anexos2}')
