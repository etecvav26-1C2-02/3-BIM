"""
    Auor: Daniel de Sousa Araujo, Miguel marcelo 
    Data: Agosto/2026
    Descrição: Lê dois números inteiros e informa qual é o maior ou se são iguais.
"""
numero = int(input ("Digite um numero inteiro positivo: "))
i = 1
soma = 0


if numero > 0:
    while i <= numero:
        if i % 2 == 0:
            soma = soma + i 
        i += 1
    print ("Soma dos pares é: ", soma )          

else:
    print("Numero invalido. Digite um valor positivo.")
