# Autores: Miguel Marcelo e Daniel Araujo
# Finalidade: Calcular o fatorial de um número inteiro positivo
# informado pelo usuário.

numero = int (input ("escreva um numero inteiro positivo: "))
i = 1
fatorial = 1

# Repete enquanto o número for positivo e o contador
# for menor ou igual ao número informado.
while (numero > 0 and i <= numero):

    # Multiplica o valor do fatorial pelo contador atual.
    fatorial = fatorial * i

    # Aumenta o contador em 1 para continuar o cálculo.
    i += 1

# Exibe o número informado e o resultado do seu fatorial.
print("o número ",numero, "em fatorial é : ",fatorial)
