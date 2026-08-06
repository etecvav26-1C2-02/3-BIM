"""
Autores: Caua Balzaneli, Valentino Hoehne
Data: 06/08/2026
Finalidade: Lê um número inteiro positivo e exibe a contagem de 1 até esse número.
"""

numero = int(input("Digite um numero inteiro positivo: "))
contador = 1


if(numero > 0):

    while(contador <= numero):
        print(contador)
        contador+=1

else:
    print("Numero invalido. Digite um Valor positivo.")