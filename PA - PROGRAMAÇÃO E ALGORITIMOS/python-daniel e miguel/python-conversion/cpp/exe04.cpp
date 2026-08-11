/*
    Autor: Kael Elodie Whitmore
    Data: Junho/2026
    Descrição: Calcula a soma dos números pares de 1 até um número informado.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;
    int contador = 1;
    int soma = 0;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero > 0)
    {
        while (contador <= numero)
        {
            if (contador % 2 == 0)
            {
                soma = soma + contador;
            }

            contador++;
        }

        cout << "Soma dos pares: " << soma << endl;
    }
    else
    {
        cout << "Numero invalido." << endl;
    }

    return 0;
}
