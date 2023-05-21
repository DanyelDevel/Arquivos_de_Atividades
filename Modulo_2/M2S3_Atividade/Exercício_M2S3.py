import sqlite3
conn =  sqlite3.connect("database.db")
c = conn.cursor()

sql_cliente ='''
CREATE TABLE cliente (
    id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
    nome TEXT(100),
    cpf TEX(14) NOT NULL,
    CONSTRAINT cliente_UN UNIQUE (cpf)
);'''
c.execute(sql_cliente)

sql_pedido ='''
CREATE TABLE pedido (
    id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
    "data" TEXT(20) NOT NULL,
    cliente_id INTEGER NOT NULL,
    CONSTRAINT pedido_FK FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);'''
c.execute(sql_pedido)

sql_item_pedido ='''
CREATE TABLE item_pedido (
    id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto TEX(100),
    valor REAL,
    quantidade INTEGER,
    CONSTRAINT item_pedido_FK FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);'''
c.execute(sql_item_pedido)

conn.commit()
conn.close()