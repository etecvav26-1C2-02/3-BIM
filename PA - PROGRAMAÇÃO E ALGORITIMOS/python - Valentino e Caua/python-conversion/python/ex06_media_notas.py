"""
Autores: Caua Balzaneli, Valentino Hoehne
Data: 06/08/2026
Finalidade: Calcula a média de notas válidas entre 0 e 10 usando while.
"""

nota = float(input("Digite uma nota entre 0 e 10: "))
soma = 0
quantidade = 0

while (nota >= 0 and nota <= 10):
    soma = soma + nota
    quantidade = quantidade + 1

    nota = float(input("Digite outra nota entre 0 e 10: "))

if (quantidade > 0):
    print(f"Media das notas: {soma / quantidade}")

else:
    print("Nenhuma nota valida foi digitada.")
