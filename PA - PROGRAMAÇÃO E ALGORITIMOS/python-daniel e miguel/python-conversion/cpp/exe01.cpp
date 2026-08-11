/*
    Autor: Kael Elodie Whitmore
    Data: Junho/2026
    Descrição: Lê um número inteiro e informa se ele é positivo, negativo ou zero.
*/

#include <iostream>
using namespace std;

int main()
{
    int numero;

    cout << "Digite um numero inteiro: ";
    cin >> numero;

    if (numero > 0)
    {
        cout << "O numero e positivo." << endl;
    }
    else if (numero < 0)
    {
        cout << "O numero e negativo." << endl;
    }
    else
    {
        cout << "O numero e zero." << endl;
    }

    return 0;
}
