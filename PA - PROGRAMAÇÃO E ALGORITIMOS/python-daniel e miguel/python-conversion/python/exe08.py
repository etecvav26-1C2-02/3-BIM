"""
    Autor: Daniel de sousa Araujo,MIguel Marcelo
    Data: Junho/2026
    Descrição: Verifica se um número inteiro positivo é primo.
"""
numero = int(input("Digite uma numero inteiro positivo: "))
divisor= 1
quantidadeDivisores = 0

if numero > 0:
    while divisor <= numero:
        if numero % divisor == 0:
            quantidadeDivisores += 1
        divisor += 1
    if quantidadeDivisores == 2:
      print("O número é primo.")
    else:
      print("O número não é primo.")
else:
    print("O número não é primo.(invalido)")
