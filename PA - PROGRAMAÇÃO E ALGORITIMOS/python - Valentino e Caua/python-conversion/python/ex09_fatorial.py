"""
Autores: Caua Balzaneli, Valentino Hoehne
Data: 06/08/2026
Finalidade: Calcula o fatorial de um número inteiro positivo.
"""

numero = int(input("Digite um numero inteiro positivo: "))
contador = 1
fatorial = 1

if (numero >= 0):

    while (contador <= numero):
        fatorial = fatorial * contador
        contador = contador + 1

    print(f"Fatorial: {fatorial}")

else:
    print("Numero invalido.")
