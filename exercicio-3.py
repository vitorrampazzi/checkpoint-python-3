def analisar_texto(texto):
    pontuacao = '!"#$%&()*+,-.:;<=>][/?@^_`{|}~'
    for simbolo in pontuacao:
        texto = texto.replace(simbolo, '')

    palavras = texto.lower().split()

    frequencias = {}
    for palavra in palavras:
        if len(palavra) >= 3:
            if palavra in frequencias:
                frequencias[palavra] += 1
            else:
                frequencias[palavra] = 1

    frequencias = list(frequencias.items())

    for i in range(len(frequencias)):
        for j in range(i + 1, len(frequencias)):
            if frequencias[i][1] < frequencias[j][1]:
                frequencias[i], frequencias[j] = frequencias[j], frequencias[i]

    return frequencias

print(analisar_texto('O texto, o texto, esta sendo analisado, analisado, texto, esta sendo'))
