# Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
#   ° As tarefas devem ser divididas em “categorias”;
#   ° Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
#   ° As restrições/relacionamentos devem fazer sentido.

#Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
#   ° Eventos devem ter título, data e local, além da referência ao organizador;
#   ° O organizador deve ter nome, email e cpf;
#   ° As restrições/relacionamentos devem fazer sentido.


import sqlite3
conn = sqlite3.connect('Gerenciador.db')
c = conn.cursor()

# Tabela de categoria
c.execute('''
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY,
    título TEXT NOT NULL UNIQUE
);
''')

# Tabela de Gerenciamento de tarefas
c.execute('''
CREATE TABLE tarefas (
    id INTEGER PRIMARY KEY,
    título TEXT NOT NULL,
    data_do_evento TEXT,
    status INTEGER CHECK (status IN (0, 1)),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);  
''')

conn.commit()
conn.close()