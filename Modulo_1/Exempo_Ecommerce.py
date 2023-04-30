# Implementando a leitura de informações dos produtos

estoque = {} # Armazenamento de produtos

for i in range(2):
    codigo = int(input("Digite o código: "))
    categoria = input("Digite a categoria: ")
    nome = input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    preco = float(input("Digite o preço: "))

    produto =  {"Código": codigo,"Produto": nome, "Descrição": descricao, "Preço": preco}

    # Implementando a criação de categoria ou inclusão de produto
if categoria not in estoque:
        estoque[categoria] = []
        estoque[categoria].append(produto)
else:
        estoque[categoria].append(produto)

if categoria in estoque:
    for ptoduto in estoque[categoria]:
        print("------------------------------")
        print("----Informações do produto----")
        print("------------------------------")
        print(f"Código: {produto['Código']}")
        print(f"Categoria: {categoria}")
        print(f"Nome: {produto['Produto']}")
        print(f"Descrição: {produto['Descrição']}")
        print(f"Preço: {produto['Preço']}")

# Implementando o cadastro do produto


# Implementando o menu de interação

# Implementando a consulta de produtos

# implementando o filtro de produtos por preços
