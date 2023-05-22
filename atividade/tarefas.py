import sqlite3
conn = sqlite3.connect('Lista_Tarefas.sqlite3')
c = conn.cursor()

print("""O que deseja fazer? \n
[1] criar nova tarefa
[2] atualizar tarefa
[3] excluir tarefa
[4] sair
""")
funcao = int(input())

def criar_tarefa():
    quantidade = str(input("""Qual a quantidade? """))
    for i in range(quantidade):
        nome = input('Digite o nome da tarefa: ')
        data = str(input('Digite o data da tarefa: '))
        status = input('Digite o status da tarefa: ')
        cat_id = c.execute("SELECT id FROM Categorias")
        for categoria in cat_id:
            print(categoria)
        categoria_id = input('Digite o id da categoria da tarefa: ')
        sql_criar = "INSERT INTO tarefas(nome, data, conclusao, categorias_id) values (?, ?, ?, ?)"
        c.execute(sql_criar, [nome, data, status, categoria_id])
def atualizar_tarefa():
    id = c.execute("SELECT id FROM tarefas")
    for tarefa in id:
        print(tarefa)
    print('Qual o id da tarefa? ')
    tarefa_id = int(input())
    print("""O que deseja atualizar? \n
    [1] nome da tarefa
    [2] data da tarefa
    [3] status da tarefa
    [4] categoria da tarefa
    [5] sair
    """)
    funcao = int(input())
    if funcao == 1:
        quantidade = str(input("""Qual a quantidade? """))
        for i in range(quantidade):
            nome = input('Digite o nome da tarefa: ')
            sql_atualizar = "UPDATE tarefas SET nome = ? WHERE id = ?"
            c.execute(sql_atualizar, [nome, tarefa_id])
    if funcao == 2:
        quantidade = str(input("""Qual a quantidade? """))
        for i in range(quantidade):
            data = int(input('Digite o data da tarefa: '))
            sql_atualizar = "UPDATE tarefas SET data = ? WHERE id = ?"
            c.execute(sql_atualizar, [data, tarefa_id])
    if funcao == 3:
        quantidade = str(input("""Qual a quantidade? """))
        for i in range(quantidade):
            status = input('Digite o status da tarefa: ')
            sql_atualizar = "UPDATE tarefas SET conclusao = ? WHERE id = ?"
            c.execute(sql_atualizar, [status, tarefa_id])
    if funcao == 4:
        quantidade = str(input("""Qual a quantidade? """))
        for i in range(quantidade): 
            id = c.execute("SELECT categorias_id FROM tarefas")
            for tarefa in id:
                print(tarefa)
            categoria = int(input('Digite o id da tarefa: '))
            sql_atualizar = "UPDATE tarefas SET categoria_id = ? WHERE id = ?"
            c.execute(sql_atualizar, [sql_atualizar, categoria])
    if funcao == 4:
        quit()
def excluir_tarefa():
    quantidade = str(input("""Qual a quantidade? """))
    for i in range(quantidade):
        tarefa = c.execute("SELECT categorias_id FROM tarefas")
        for excluir in tarefa:
            print(excluir)
        tarefa_id = int(input('Digite o id da tarefa: '))
        sql_excluir = "DELETE FROM tarefas WHERE id = ?"
        c.execute(sql_excluir,[tarefa_id])


if funcao == 1:
    criar_tarefa()
if funcao == 2:
    atualizar_tarefa()
if funcao == 3:
    excluir_tarefa()
if funcao == 4:
    quit()

conn.commit()
conn.close()