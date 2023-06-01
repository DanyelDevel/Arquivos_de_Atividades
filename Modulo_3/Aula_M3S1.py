#  Criando um contador com While
#
'''
i=0
while i<10:
    i=i+1
    print(i)

# Criando uma iteração de contagem
#
lista=[]
i=0
while i<10:
    i=i+1
    lista.append(i)
for i in lista:
    print(i)

# Criando iteração de contagem com renge
#
for i in range(10):
    print(i)

# Criando uma classe iterável para contagem
#
class Contar:
    def __init__(self, maximo = 10000):
        self.elementoAtual = 0
        self.maximo = maximo
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.elementoAtual >= self.maximo:
            raise StopIteration
        retorno = self.elementoAtual
        self.elementoAntigo = retorno
        self.elementoAtual = self.elementoAtual + 1
        
        return retorno
    def __str__(self):
        return f"estou contando: {self.elementoAtual}"
    
# Fazendo teste
#
c = Contar()

# Dê vários Shift+Enter para ver o que acontece
#
c.__next__()

# Observe a diferença no print do i e do c
#
c2 = Contar(10)
for i in c2:
    print(i)

c3 = Contar(10)
for i in c3:
    print(c3)

# Criando uma classe iterável para fazer a sequência de Fibonacci
#
class Fibonacci:
    def __init__(self, maximo = 100000):
        self.elementoAtual = 0
        self.proxElemento = 1
        self.maximo = maximo
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.elementoAtual > self.maximo:
            raise StopIteration
            
        retorno = self.elementoAtual
        self.elementoAtual = self.proxElemento
        self.proxElemento = self.proxElemento + retorno
        
        return retorno
    
    def __str__(self):
        return f"{self.elementoAtual}"

# Alguns testes
#
f = Fibonacci()

# Dê vários Shift+Enter para ver o que acontece
#
f.__next__()

# Fibonacci até alcançar 100
#
f2 = Fibonacci(100)
for i in f2:
    print(i)

# Usando iteradores para a lógica de um estacionamento
#
class Carro:
    def __init__(self, placa, cor, modelo):
        self.placa = placa
        self.cor = cor
        self.modelo = modelo
    def __str__(self):
        return f"Carro do modelo {self.modelo}, da cor {self.cor}, com o emplacameto {self.placa} "
    
carro = Carro("abc_1234", " azul", "Fusca")   
print(carro)

# Preparando a classe Estacionamento para receber os carros
#
class Estacionamento:
    def __init__(self, vagas = 0):
        self.numero_vagas = vagas
        self.carros = []
        self.passo = 0
    
    def adicionar_carro(self, carro):
        if self.numero_vagas > len(self.carros):
            self.carros.append(carro)
        else:
            print("Estacionamento cheio")
    
    def __iter__(self):
        self.passo = 0
        return self
        
    def __next__(self):
        if self.passo >= len(self.carros):
            raise StopIteration
        else:
            resposta = self.carros[self.passo]
            self.passo = self.passo + 1
            return resposta
            
        return 1
    
esta_verm = Estacionamento(5)

carro = Carro("abc_1234", "preto", "Fusca")
esta_verm.adicionar_carro(carro)

for car in esta_verm:
    print(car)

for car in esta_verm:
    print(esta_verm)

# Criando um generador para a sequência de Fibonacci
#
def fibonacci_g(maximo):
    elementoAtual = 0
    proximoElemento = 1
    num_it = 0
    
    while num_it < maximo:
        yield elementoAtual    
        elementoAntigo = elementoAtual
        elementoAtual = proximoElemento
        proximoElemento = elementoAntigo + proximoElemento
        num_it = num_it + 1
for i in fibonacci_g(10):
    print(i)
'''
# Usando as Requests para acessar a página web e obter modelos de carros
#
import  requests

class Modelos:
    def __init__(self, codigo: str):
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']
            self.passo = 0
            self.tamanho = len(self.modelos)
        else:
            print('Falha ao carregar')
    def __iter__(self):
        self.passo = 0
        return self
    def __next__(self):
        if self.passo >= self.tamanho:
            raise StopIteration
        resposta = list(self.modelos)[self.passo]
        self.passo = self.passo + 1
        return resposta

mod = Modelos('1')
for m in mod:
    print(m)
