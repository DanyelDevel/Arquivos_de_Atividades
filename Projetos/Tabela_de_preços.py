# Estrutura de Tabela de Preços com adição de novos itens e seus preços
'''
produtos = ["Arroz", "Feijão", "Macarrão","Maçã", "Banana"]
precos = ["15,49", "11,59", "5,99", "8,99", "7,59"]
tabela = len(produtos)

for i in range(tabela):
    print(i,")",produtos[i],": ", precos[i])
'''

# Estrutura de Tabela de Preços com adição de novos itens e consulta filtrada
estoque =  {} # Armazenamento do produto

# Adição dos dados no sistema
for i in range(2):
    codigo = int(input("Digite o código: "))
    categoria = input("Digite a categoria: ")
    nome = input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    preco = float(input("Digite o preço: "))

# Dados do produto
produto = {"codigo": codigo, "produto": nome, "descricao": descricao, "preco": preco}

# Criação de categorias ou adição de produtos na categoria
if categoria not in estoque:
    estoque[categoria] = []
    estoque[categoria].append(produto)
else:
    estoque[categoria].append(produto)

# Visualização das informações
for categoria in estoque:
    for produto in estoque[categoria]:
        print("------------------------------")
        print("----Informações do produto----")
        print("------------------------------")
        print(f"Código: {produto['codigo']}")
        print(f"Categoria: {categoria}")
        print(f"Nome: {produto['produto']}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Preço: {produto['preco']}")

