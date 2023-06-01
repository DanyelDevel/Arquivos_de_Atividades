def decorator_imprimir(funcao):
    def primeira_funcao():
        capital = 1000
        taxa = 5
        tempo = 6
        resultado = funcao(capital, taxa, tempo)
        print(f'CAPITAL = {capital} TAXA = {taxa} TEMPO = {tempo} \n{resultado}')
    return primeira_funcao
@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) *tempo
juros_simples()