```python
# Autores: Miguel Marcelo e Daniel Araujo
# Finalidade: Identificar se o número inteiro informado pelo usuário é positivo,
# negativo ou igual a zero.

numero = int(input("digite um número inteiro: "))

# Verifica se o número é maior que zero.
if numero > 0:
    print("o numero é positivo! ")

# Caso o número não seja maior que zero, verifica se ele é menor que zero.
elif numero < 0:
    print("o numero é negativo! ")

# Se não for maior nem menor que zero, significa que o número é igual a zero.
else:
    print("o número é 0! ")
```
