# Autores: Miguel Marcelo e Daniel Araujo
# Finalidade: Ler 10 números inteiros e contar quantos são positivos,
# negativos e iguais a zero.

positivo = 0
negativo = 0
zero = 0
i = 1

# Repete o processo até que 10 números sejam analisados.
while i <= 10:
    # Solicita ao usuário um número inteiro.
    numero = int(input(f"Digite o {i}º número: "))

    # Verifica se o número é positivo.
    if numero > 0:
        positivo += 1

    # Verifica se o número é negativo.
    elif numero < 0:
        negativo += 1

    # Caso não seja positivo nem negativo, o número é zero.
    else:
        zero += 1

    # Aumenta o contador para passar para o próximo número.
    i += 1

# Exibe a quantidade de números positivos.
print("Positivos:", positivo)

# Exibe a quantidade de números negativos.
print("Negativos:", negativo)

# Exibe a quantidade de números iguais a zero.
print("Zeros:", zero)

