/*
   Autores: Caua Balzaneli, Valentino Hoehne
   Data: 06/08/2026
   Finalidade: Calcula o fatorial de um número inteiro positivo.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;
    int contador = 1;
    int fatorial = 1;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero >= 0)
    {
        while (contador <= numero)
        {
            fatorial = fatorial * contador;
            contador++;
        }

        cout << "Fatorial: " << fatorial << endl;
    }
    else
    {
        cout << "Numero invalido." << endl;
    }

    return 0;
}
