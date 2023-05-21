import sqlite3
conn = sqlite3.connect('Lista_Tarefas.sqlite3')
c = conn.cursor()
print('''O que deseja fazer? \n
[1] listar afazeres
[2] listar categorias
[3] sair
''')
funcao = int(input())
def lista_afazeres():
    print('''Selecione uma opção: \n
    [1] lista completa
    [2] lista por datas
    [3] lista de conclusão
    [4] sair
    ''')
    opcao = int(input())
    if opcao == 1:
        tarefas = c.execute("SELECT * FROM tarefas")
        for completa in tarefas:
            print(completa)
    if opcao == 2:
        data = str(input('Digite a data desejada: '))
        lista = "SELECT * FROM tarefas WHERE data = ?'"
        datas = c.execute(lista, [data])
        for dados in datas:
            print(dados)
    if opcao == 3:
        conclusao = c.execute('SELECT * FROM tarefas WHERE conclusao = concluido')
        for lista in conclusao:
            print(lista)
    if opcao == 4:
        quit()
def lista_categ():
    categorias = c.execute('SELECT * FROM Categorias')
    for lista in categorias:
        print(lista)
if funcao == 1:
    lista_afazeres()
if funcao == 2:
    lista_categ()
if funcao == 3:
    quit()
