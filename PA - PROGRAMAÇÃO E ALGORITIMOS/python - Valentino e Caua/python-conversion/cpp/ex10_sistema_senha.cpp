/*
   Autores: Caua Balzaneli, Valentino Hoehne
   Data: 06/08/2026
   Finalidade: Simula um sistema simples de senha com até 3 tentativas.
*/

#include <iostream>
using namespace std;

int main()
{
    int senha;
    int senhaCorreta = 1234;
    int tentativas = 1;
    int limiteTentativas = 3;

    cout << "Digite a senha: ";
    cin >> senha;

    while (senha != senhaCorreta && tentativas < limiteTentativas)
    {
        cout << "Senha incorreta. Tente novamente: ";
        cin >> senha;

        tentativas++;
    }

    if (senha == senhaCorreta)
    {
        cout << "Acesso liberado." << endl;
    }
    else
    {
        cout << "Acesso bloqueado." << endl;
    }

    return 0;
}
