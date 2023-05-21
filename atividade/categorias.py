import sqlite3
conn = sqlite3.connect('Lista_Tarefas.sqlite3')
c = conn.cursor()

print("""O que deseja fazer? \n
[1] criar categoria
[2] atualizar categoria
[3] excluir categoria
""")
funcao = int(input())

def criar_categ():
    nome = input('Digite o nome da categoria: ')
    sql_criar = "INSERT INTO Categorias(nome) values (?)"
    c.execute(sql_criar, [nome])

def atualizar():
    cat_existentes = c.execute("SELECT * FROM Categorias")
    for categoria in cat_existentes:
        print(categoria)
    id = int(input('Digite o id: '))
    nome = input('Digite a nova categoria: ')
    sql_atualizar = "UPDATE Categorias SET nome = ? WHERE id = ?"
    c.execute(sql_atualizar, [nome, id])

def excluir_cat():
    cat_existentes = c.execute("SELECT * FROM Categorias")
    for categoria in cat_existentes:
        print(categoria)
    id = int(input('Digite o id: '))
    sql_excluir = "DELETE FROM Categorias WHERE id = ?"
    c.execute(sql_excluir, [id])

if funcao == 1:
    criar_categ()

if funcao == 2:
    atualizar()

if funcao == 3:
    excluir_cat()

conn.commit()
conn.close()