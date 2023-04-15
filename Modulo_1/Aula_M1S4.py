# INDICE    0          1          2          3
"""
nomes = ['Junior', 'Wyllon', 'Kamilla', 'Carlos']
print(nomes[2])

for indice in range(4):
    print(nomes[indice])"""

# INDICE    0          1          2          3
'''
nomes = ['Junior', 'Wyllon', 'Kamilla', 'Carlos', 'Sherlon', 'Joao']
#len() -> length - > Tamanho/Comprimento

tam = len(nomes)
for indice in range(tam):
    print(indice, nomes[indice])'''


'''
for indice,valor in enumerate['Junior', 'Wyllon', 'Kamilla', 'Carlos', 'Sherlon', 'Joao']
    print(indice,valor)'''


'''
nomes = [] # Armazene as informacoes dos clientes
for i in range(5):
    nome = input('Digite o seu nome: ')
    nomes.append(nome)
    print(nomes, len(nomes))'''


'''
nomes = ['Junior', 'Wyllon', 'Kamilla', 'Carlos', 'Sherlon', 'Joao']
print(nomes)
nomes[0] = 'Rafael'
print(nomes)'''


'''
#TUPLAS (Imutáveis)
nomes = ['Junior', 'Wyllon', 'Kamilla', 'Carlos', 'Sherlon', 'Joao']
print(nomes)
nomes[0] = 'Rafael'
print(nomes)'''


# DICIONÁRIOS {chave: valor}
'''
cliente = {'Nome': 'Sherlon', 'Idade': 27, 'Senha': 'senha123'}

cliente['Nome'] = 'Wyllon'
print(cliente['Nome'])
print(cliente['Idade'])'''


# DICIONÁRIOS {chave: valor}
'''
cliente = {'Nome': 'Sherlon', 'Idade': 27, 'Senha': 'senha123'}

senha_digitada = 'lalala'
if cliente['Senha'] == senha_digitada:
    print('login realizado')
else:
    print('Senha invalida')
    cliente['Senha'] = input('Digite a nova senha: ')
print(cliente)'''


'''
cliente = {'Nome': 'Sherlon', 'Idade': 27, 'Senha': 'senha123'}
print(cliente.keys())
print(cliente.values())
print(cliente.items())'''


'''
def exemplo(cliente):
    print(cliente, type(cliente))


cliente = [1,2,3,4,5,6,4,8]
exemplo(cliente)'''

'''
class Cliente:
    def __init__(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None

    def cadastro(self):
        self.nome  = None
        self.cpf   = None
        self.idade = None
    
    def mostrar_dados(self):
        print('Nome: ',self.nome)
        print('CPF: ',self.cpf)
        print('Idade: ',self.idade)

#
joao = Cliente()
joao.cadastro()
joao.mostrar_dados()'''
