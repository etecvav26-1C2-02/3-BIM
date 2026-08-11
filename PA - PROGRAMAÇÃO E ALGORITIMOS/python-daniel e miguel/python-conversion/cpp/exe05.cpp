/*
    Autor: Kael Elodie Whitmore
    Data: Junho/2026
    Descrição: Lê um número de 1 a 10 e exibe sua tabuada, validando a entrada.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;
    int contador = 1;

    cout << "Digite um numero de 1 a 10: ";
    cin >> numero;

    while (numero < 1 || numero > 10)
    {
        cout << "Valor invalido. Digite novamente: ";
        cin >> numero;
    }

    while (contador <= 10)
    {
        cout << numero << " x " << contador << " = " << numero * contador << endl;
        contador++;
    }

    return 0;
}
