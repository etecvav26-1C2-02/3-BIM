"""
    Auor: Daniel de Sousa Araujo, Miguel marcelo 
    Data: Junho/2026
    Descrição: Lê dois números inteiros e informa qual é o maior ou se são iguais.
"""

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

if numero1 > numero2: 
    print("O maior numero é: ", numero1 ,"\n") 
elif numero2 > numero1:
   print("O maior numero é: ", numero2 ,"\n")   
else:
    print("Os numeros são iguais")
