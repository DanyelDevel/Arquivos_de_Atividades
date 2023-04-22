import sqlite3

conexao = sqlite3.connect("db.sqlite3")
cursor = conexao.cursor()
sql = """   CREATE TABLE funcionarios (
            id INT PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            data_cadastro DATE NOT NULL,
            endereço TEXT NOT NULL
            );
            """


cursor.execute(sql)
conexao.commit()
conexao.close()
