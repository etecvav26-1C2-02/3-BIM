# Autores: Miguel Marcelo e Daniel Araujo
# Finalidade: Mostrar na tela todos os números inteiros de 1 até o número
# informado pelo usuário, caso ele seja positivo.

numero = int(input("Qual seu número? "))

# Verifica se o número informado é maior que zero.
if numero > 0:
    # Inicia o contador em 1.
    i = 1

    # Repete enquanto o contador for menor ou igual ao número informado.
    while i <= numero:
        # Exibe o valor atual do contador.
        print(i)

        # Aumenta o contador em 1 a cada repetição.
        i += 1
        
# Caso o número seja zero ou negativo, exibe uma mensagem de erro.
else:
    print("Número inválido")
```
