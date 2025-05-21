def eh_perfeito(n):
    def somar_divisores(n, divisor):
        if divisor == 0:
            return 0
        elif n % divisor == 0:
            return divisor + somar_divisores(n, divisor - 1)
        else:
            return somar_divisores(n, divisor - 1)

    return somar_divisores(n, n - 1) == n

def numeros_perfeitos_ate_n(N):
    numeros_perfeitos = []
    for numero in range(2, N + 1):
        if eh_perfeito(numero):
            numeros_perfeitos.append(numero)
    return numeros_perfeitos

N = int(input("Digite um número N: "))
if N <= 5:
    print("Sem números perfeitos")
else:
    print(f"Números perfeitos até {N} : {numeros_perfeitos_ate_n(N)}")
