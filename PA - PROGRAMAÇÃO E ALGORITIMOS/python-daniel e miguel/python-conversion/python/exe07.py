# Autores: Miguel e Daniel
# Finalidade: contar quantos números positivos, negativos e zeros
# foram digitados pelo usuário.

positivo = 0
negativo = 0
zero = 0
i = 1

while i <= 10:
    # Pede 10 números ao usuário
    numero = int(input(f"Digite o {i}º número: "))

    # Verifica se o número é positivo
    if numero > 0:
        positivo += 1

    # Verifica se o número é negativo
    elif numero < 0:
        negativo += 1

    # Se não for positivo nem negativo, é zero
    else:
        zero += 1

    i += 1

# Mostra os resultados
print("Positivos:", positivo)
print("Negativos:", negativo)
print("Zeros:", zero)
