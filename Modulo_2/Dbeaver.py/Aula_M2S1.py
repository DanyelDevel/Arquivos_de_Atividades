# CRIAR UMA TABELA CHAMADA "LIVROS" COM OS SEGUINTES CAMPOS:
# id(inteiro), título(texto), autor(texto), data_de_publicação(data), preço(decimal)
# O CAMPO ID DEVE SER A CHAVE PRIMÁRIA

# Biblioteca responsável por interagir com o banc de dados
import sqlite3

# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Criar a tabela de categorias
c.execute('''CREATE TABLE livros (
    id INT PRIMARY KEY,
    título VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    data_de_publicação DATE,
    preço DECIMA(10, 2)
);

''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
