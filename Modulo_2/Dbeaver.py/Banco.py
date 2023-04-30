'''
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
'''

#PROJETO COM ERRO
'''
import sqlite3
conexao = sqlite3.connect('database')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE funcionario (id INT, nome VARCHAR(100), cpf VARCHAR(100), data_cadastro VARCHAR(100), endereço VARCHAR(100)',
'INSERT INTO funcionario values(1, 'Danilo', '111111111111', '05/10/2022', 'RIO TINTO')'

SELECT * from funcionario;)
conexao.commit()
conexao.close()
'''

import sqlite3
conexao = sqlite3.connect('db.sqlite3')
sql = conexao.cursor()

sql.execute('''CREATE TABLE categoria (
        id INT NOT NULL,
        nome VARCHAR(100),
                PRIMARY KEY (id)
);

        CREATE TABLE produto (
                id INT NOT NULL,
                nome VARCHAR(100),
                categoria_id INT NOT NULL,
                        PRIMARY KEY (id),
                        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
        );
''')

conexao.commit()
conexao.close()