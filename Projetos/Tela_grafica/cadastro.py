from PySimpleGUI import  PySimpleGUI as sg

# Layout
# Tema do PySimpleGUI
sg.theme('Reddit')

# Configuração do Layout (linhas e colunas)
layout = [
    # linha de dados de usuário
    [sg.Text('Usuário'), sg.Input(key ='Usuário', size = (20,15))],
    # linha de senha de usuário
    [sg.Text('Senha'), sg.Input(key  ='Senha', password_char='*', size = (20,15))],
    # linha de salvar senha
    [sg.Checkbox('Salvar o login?')],
    # linha de login
    [sg.Button('Entrar')]
]
#Janela
# Criação da janela
janela = sg.Window('Login', layout)
#Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'danyel' and valores['Senha'] == '123456':
            print('Login Concluido')
            break