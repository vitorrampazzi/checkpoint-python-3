def criptografar(texto, chave):
    alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    deslocado_min = alfabeto_min[chave:] + alfabeto_min[:chave]
    deslocado_mai = alfabeto_mai[chave:] + alfabeto_mai[:chave]


    texto_traducao = str.maketrans(alfabeto_min + alfabeto_mai, deslocado_min + deslocado_mai)

    return texto.translate(texto_traducao)


print(criptografar('Amanha eu vou jogar basquete com meus amigos fora de casa no sesc', 7))
