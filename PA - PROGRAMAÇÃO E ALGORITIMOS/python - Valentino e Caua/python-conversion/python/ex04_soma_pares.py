"""
Autores: Caua Balzaneli, Valentino Hoehne
Data: 06/08/2026
Finalidade: Calcula a soma dos números pares de 1 até um número informado.
"""

numero = int(input("Digite um numero inteiro positivo: "))
contador = 1
soma = 0

if(numero > 0):

    while (contador <= numero):
        if(contador % 2 == 0 ):
            soma = soma + contador

        contador+=1

    print(f"Soma dos pares: {soma} ")

else:
    print("Numero invalido")







