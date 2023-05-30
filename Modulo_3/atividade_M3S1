import  requests

class IteratorFIPE:
    def __init__(self, codigo: str):
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos"
        self.modelo = requests.get(url).json()["modelos"]
        self.codigo = codigo
        self.indice = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.indice < len(self.modelo):
            modelo = self.modelo[self.indice]
            self.indice +=1
            return {"nome": modelo["nome"],"id": modelo["codigo"]}
        else:
            print('Fim da interação')
            raise StopIteration
iterator = IteratorFIPE(15)  #Daewoo
for modelo in iterator:
    print(modelo)