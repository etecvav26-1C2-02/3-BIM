/*
   Autores: Caua Balzaneli, Valentino Hoehne
   Data: 06/08/2026
   Finalidade: Lê um número inteiro positivo e exibe a contagem de 1 até esse número.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;
    int contador = 1;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero > 0)
    {
        while (contador <= numero)
        {
            cout << contador << endl;
            contador++;
        }
    }
    else
    {
        cout << "Numero invalido. Digite um valor positivo." << endl;
    }

    return 0;
}
