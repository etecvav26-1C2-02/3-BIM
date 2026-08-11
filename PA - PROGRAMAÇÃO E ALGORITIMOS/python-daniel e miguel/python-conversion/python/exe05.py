# Autores: Miguel Marcelo e Daniel Araujo
# Finalidade: Verificar se o número informado está entre 1 e 10 e,
# em seguida, mostrar a tabuada desse número.

numero = int(input("fale um número de 1 a 10? "))
i = 1

# Verifica se o número está fora do intervalo permitido (1 a 10).
while numero < 1 or numero > 10:
  # Solicita um novo número caso o anterior seja inválido.
  numero = int (input ("seu número é invalido. tente novamente: "))

# Repete o processo enquanto o contador for menor ou igual a 10.
while i <= 10:
    # Mostra a multiplicação do número pelo valor atual do contador.
    print(numero, "x", i, "=", numero * i, "\n")

    # Aumenta o contador em 1 para passar para a próxima multiplicação.
    i += 1
