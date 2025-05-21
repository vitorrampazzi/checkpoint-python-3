produtos = []

while True:
    nome = input('Escreva o nome do produto (Ou escreva SAIR para sair do programa)')
    if nome.lower() == 'sair':
        print('Programa finalizado')
        break
    else:
        preco = int(input('Escreva o preço do produto.'))
        categoria = input('Escreva a categoria do produto')

        produto = {
            'nome': nome,
            'preco': preco,
            'categoria': categoria
        }
        produtos.append(produto)

    maior_preco = produtos[0]['preco']
    menor_preco = produtos[0]['preco']

    for produto in produtos:
        if produto['preco'] > maior_preco:
            produto_caro = produto['preco']
        if produto['preco'] < menor_preco:
            menor_preco = produto['preco']

    media = sum(produto['preco'] for produto in produtos) / len(produtos)

    print(f"nome: {produto['nome']}, preço: {produto['preco']}, categoria: {produto['categoria']}")
    print(f'A média de produtos é {media}')
    print(f'O maior preço é {maior_preco}, e o menor preço é {menor_preco}')
