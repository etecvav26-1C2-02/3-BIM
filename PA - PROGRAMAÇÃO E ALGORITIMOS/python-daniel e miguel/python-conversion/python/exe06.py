"""
    Auor: Daniel de Sousa Araujo, Miguel marcelo 
    Data: Agosto/2026
    Descrição: Calcula a média de notas válidas entre 0 e 10 usando while.
"""
nota = float(input("Digite uma nota entre 0 e 10: "))
quantidade = 0
soma = 0

while nota > 0 and nota <= 10:
    soma = soma + nota
    quantidade += 1
    nota = float(input("Digite outra nota ou um número fora de 0-10 para sair: "))
    
if quantidade > 0: 
    print("Média das notas: ", soma / quantidade)
else:
    print("Nenhuma nota válida foi digitada.")
