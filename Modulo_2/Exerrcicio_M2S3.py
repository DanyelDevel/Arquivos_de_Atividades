#- Utilizando o comando INSERT, insira mais dois novos fornecedores:“Padaria do Pão” e “Marcenaria Martelo”, com os ids 3 e 4 respectivamente, e crie também os endereços;
#- Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;
#- Selecione todos os registros da tabela fornecedor com o comando SELECT;
#- Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;
#- Remova o fornecedor que tem o id = 1 com o comando DELETE

import sqlite3
conn =  sqlite3.connect("teste.db")
c = conn.cursor()


c.execute('''CREATE TABLE fornecedor (
            id INT,
            nome VARCHAR(150) NOT NULL,
            endereco VARCHAR(150),
            produtos VARCHAR(20)
);''')

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');")

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');")

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');")

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');")

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Padaria do Pão', 'Rua do Pão, 12', 'pães');")

c.execute("INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Marcenaria Martelo', 'Rua do Marceneiro, 55', 'madeira');")

c.execute("UPDATE fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2;")

c.execute("SELECT * FROM fornecedor;")

c.execute("SELECT * FROM fornecedor WHERE produtos = 'carnes';")

c.execute("DELETE FROM fornecedor WHERE id = 1;")

conn.commit()
conn.close()