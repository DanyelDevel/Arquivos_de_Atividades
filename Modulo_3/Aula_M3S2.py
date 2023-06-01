'''
# Trabalhando com alteração de texto
def maiusculo(texto):
    return texto.upper() # Tornar todas as letras do texto em maiúsculas
print(maiusculo('Ultima'))
mensagemMaiusculo = maiusculo
print(mensagemMaiusculo('School'))

def maiusculo(texto):
    return texto.upper() # Tornar todas as letras do texto em maiúsculas
def minusculo(texto):
    return texto.lower() # Tornar todas as letras do texto em minúsculas
def mensagem(funcao):
    texto = funcao('Ultima School')
    print(texto)
mensagem(maiusculo)
mensagem(minusculo)

# Criando um somador com decoradores
def  somador(x):
    def soma(y):
        return x+y
    return soma
resultado = somador(15)
print(resultado(10))

# Trabalhando com atribuição de argumentos com decoradores
def  cumprimento(funcao):
    def saudacao():
        print('Bom dia!')
        funcao()
        print('Boa noite!')
    return saudacao
@cumprimento
def boa_tarde():
    print('Boa tarde!')
boa_tarde()
'''
def primeiro_decorador(func): # executor do programa e atribuidor
    def primeira_func(): # funçao de atribuiçao
        print("Executar antes da funcao")
        func()  # funçao atribuida ao executor
        print("Executar depois da funcao")
    return primeira_func
@primeiro_decorador # determinador de atribuiçao de variavel
def funcao_utilizadora(): # funçao a ser atribuida
    print("Executar pela funcao")
funcao_utilizadora()