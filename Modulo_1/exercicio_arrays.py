# ESTRUTURA DE UMA LISTA COM ARMAZENAMENTO (ARRAYS)

'''
#Utilizarei os índices para demonstrar o valores da lista
#Índices     0         1        2        3         4
nomes = ["Natália", "João", "Débora", "Tiago", "Marcos"]

# Estrutura de repetição sequencial
for  i in range(4):
    #Estrutura para mostrar os nomes sequencialmente
    print(i,")", nomes[i] )
'''
'''
# Estruturando valores de RANGE correspondentes à lista
#Índices     0         1        2        3         4         5
nomes = ["Natália", "João", "Débora", "Tiago", "Marcos", "Arthur"]

#Atribuindo LENGHT(len)
tamanho = len(nomes)
# Estrutura de repetição sequencial
for  i in range(tamanho):
    #Estrutura para mostrar os nomes sequencialmente
    print(i,")", nomes[i])
'''
'''
# Estrutura de repetição com soma de índices utilizando o len

#Índices     0      1     2      3    4
valores = [15.49, 11.59, 5.99, 8.99, 7.59]
total = 0

# Estrutura de repetição sequencial
for  i in range(len(valores)):
    # Estrutura para soma
    total = total + valores[i]
    #Estrutura para mostrar os nomes sequencialmente
    print(i,")", valores[i], total )
'''