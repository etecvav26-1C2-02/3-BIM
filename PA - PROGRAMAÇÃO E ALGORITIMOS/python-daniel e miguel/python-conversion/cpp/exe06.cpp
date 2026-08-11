/*
    Autor: Miguel Marcelo, Daniel de Sousa Araujo
    Data: Junho/2026
    Descrição: Calcula a média de notas válidas entre 0 e 10 usando while.
*/

#include <iostream>
using namespace std;

int main()
{
    float nota;
    float soma = 0;
    int quantidade = 0;

    cout << "Digite uma nota entre 0 e 10: ";
    cin >> nota;

    while (nota >= 0 && nota <= 10)
    {
        soma = soma + nota;
        quantidade++;

        cout << "Digite outra nota entre 0 e 10: ";
        cin >> nota;
    }

    if (quantidade > 0)
    {
        cout << "Media das notas: " << soma / quantidade << endl;
    }
    else
    {
        cout << "Nenhuma nota valida foi digitada." << endl;
    }

    return 0;
}
