/*
    Autor: Daniel de Sousa Araujo, Miguel MArcelo
    Data: Junho/2026
    Descrição: Lê 10 números e conta quantos são positivos, negativos e zeros.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;
    int contador = 1;
    int positivos = 0;
    int negativos = 0;
    int zeros = 0;

    while (contador <= 10)
    {
        cout << "Digite o " << contador << "o numero: ";
        cin >> numero;

        if (numero > 0)
        {
            positivos++;
        }
        else if (numero < 0)
        {
            negativos++;
        }
        else
        {
            zeros++;
        }

        contador++;
    }

    cout << "Positivos: " << positivos << endl;
    cout << "Negativos: " << negativos << endl;
    cout << "Zeros: " << zeros << endl;

    return 0;
}
