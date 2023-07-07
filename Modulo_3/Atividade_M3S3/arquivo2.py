def funcao_calcular_pedido(pedido):
    cardapio = {
        100: ('Cachorro Qeunte', 9.0),
        101: ('Cachorro Quente Duplo', 11.0),
        102: ('X-Egg', 12.0),
        103: ('X-Salada', 12.0),
        104: ('X-Bacon', 14.0),
        105: ('X-Tudo', 17.0),
        200: ('Refrigerante Lata', 5.0),
        201: ('Chá Gelado', 4.0)
    }
    total = 0.0
    for codigo in pedido:
        if codigo in cardapio:
            produto, valor = cardapio[codigo]
            print(f'Voce pediu um {produto} de preco {valor:.2f}')
            total += valor 
        else:
            print('Opcao Invalida')
    return total

if __name__ == '__main__':
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)
    codigos = []
    codigo = int(input('Digite o codigo:'))

    while True:
        if codigo in [100, 101, 102, 103, 104 ,105, 200, 201]:
            codigos.append(codigo)
        else:
            print('Opcao Invalida')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

        codigo = int(input('Entre com o código desejado: '))
    total = funcao_calcular_pedido(codigo)
    print(f'O total a ser pago é: {total:.2f} R$')