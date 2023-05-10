# CRIAR UMA TABELA CHAMADA "LIVROS" COM OS SEGUINTES CAMPOS:
# id(inteiro), título(texto), autor(texto), data_de_publicação(data), preço(decimal)
# O CAMPO ID DEVE SER A CHAVE PRIMÁRIA
##
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


# Criar nova coluna de categorias na tabela livros
#
# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Comando de alteração
c.execute('''
ALTER TABLE livros ADD COLUMN categoria VARCHAR(255) NOT NULL;
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()


#  Alterre a coluna "preço" da tabela "livros" para aceitar apenas valores positivos.
#  Defina o limite mínimo de 0.0 e máximo de 9999.99.
#  Desta forma
##
"""
# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Comando de alteração
c.execute('''
        ALTER TABLE livros
        ALTER COLUMN preço DECIMAL(10, 2)
        CHECK (preço >= 0.0 AND preço <= 9999.99)
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
"""

# Ou desta forma, Crando uma pasta temporária
##
"""
# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Etapa 1: Criar uma tabela temporária com a estrutura desejada
c.execute('''
CREATE TABLE livros_temp (
    id INT PRIMARY KEY,
    título VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    data_de_publicação DATE,
    preço DECIMAL(10, 2) CHECK (preço >= 0.0 AND preço <= 9999.99)
);
''')

# Etapa 2: Copiar os dados da tabela original para a tabela temporária
c.execute('''
INSERT INTO livros_temp (id, título, autor, data_de_publicação, preço)
SELECT id, título, autor, data_de_publicação, preço FROM livros;
''')

# Etapa 3: Renomear a tabela temporária para o nome original
c.execute('''
ALTER TABLE livros_temp  RENAME TO livros;
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
"""

# Renomeie a coluna "título" da tabela "livros" para "nome_do_livro"
#
"""
# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Renomeia a coluna
c.execute('''
        ALTER TABLE livros RENAME COLUMN título TO nome_do_livro;
''')
# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
"""

# Exclua uma coluna
#

# Conectar/ criar o banco de dados
conn =  sqlite3.connect('db.sqlite3')

# Criar um objeto cursor para o comando sql
c = conn.cursor()

# Renomeia a coluna
c.execute('''
        ALTER TABLE livros DROP COLUMN data_de_publicação;
''')
# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
