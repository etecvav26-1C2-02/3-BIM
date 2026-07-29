/*
   Autores: Caua Balzaneli, Valentino Hoehne, Miguel Marcelo e Daniel de Sousa Araujo
   Data (Criacao): 28/07/2026
   Ultima Atualizacao: 28/07/2026
   Finalidade:  Um Sistema para auxiliar no acompanhamento de treinos:
                    O sistema poderá calcular IMC, registrar metas e 
                    acompanhar a evolução do aluno. 
*/


#include <iostream>
#include <string>

using namespace std;

class Cliente {
    
    private:
        int idade;
        float altura;
        float peso;
        string nome;


    public:
        // Construtor: serve para a gente preencher os dados do cliente na hora de criar ele
        Cliente(string n, int i, float a, float p) {
            nome = n;
            idade = i;
            altura = a;
            peso = p;
        }

        string GetNome() {
            return this->nome;
        }

        int GetIdade() {
            return this->idade;
        }

        int GetAltura() {
            return this->altura;
        }

        int GetPeso() {
            return this->peso;
        }
        /*
            O cálculo do IMC é feito ao dividir o peso em quilos pela altura em metros ao quadrado
            (IMC = Peso ÷ [Altura × Altura]). */
        void CalcularIMC() {
            int IMC;
            IMC = (peso / (altura * altura));
            cout << "O IMC eh: "<< IMC << endl;
        }

        void RegistrarMetas() {
            cout << "nao fizemo ainda rs";
        }

};


int main() {
    int idade;
    float altura;
    float peso;
    string nome;
    int usuario;

// --- TELA DE CADASTRO ---
    cout <<  "========================================" << endl;
    cout <<  "        SISTEMA DE ACADEMIA        " << endl;
    cout <<  "========================================" << "\n" << endl;

    cout << "Digite o nome do cliente: ";
    getline(cin, nome);
    cout << "Digite a altura do cliente (ex: 1.75): ";
    cin >> altura;
    cout << "Digite o peso do cliente (ex: 70.5): ";
    cin >> peso;
    cout << "Digite a idade do cliente: ";
    cin >> idade;
    cout << " " << endl;

    //Definindo o objeto cliente
    Cliente cliente(nome, idade, altura, peso);

    //Mostrando ao usuario os dados
    cout <<  "========================================" << endl;
    cout <<  "        DADOS DO CLIENTE        " << endl;
    cout <<  "========================================" << endl;
    cout << " " << endl;
    cout << "Nome do cliente: " << cliente.GetNome() << endl;
    cout << "Idade do cliente: " << cliente.GetIdade() << endl;
    cout << "Nome do cliente: " << cliente.GetAltura() << endl;
    cout << "Nome do cliente: " << cliente.GetPeso() << endl;

    do {
        cout << "\nO que quer fazer? " << endl;
        cout << "1. Calcular IMC"            << endl;
        cout << "2. Registrar Metas"            << endl;
        cout << "0. Sair"                        << endl;
        cout << "============================="  << endl;
        cout << "Opcao: ";
        cin >> usuario;

        switch (usuario) {
            case 1: cliente.CalcularIMC();         break;
            case 2: cliente.RegistrarMetas();         break;
            case 0: cout << "Saindo..." << endl;     break;
            default: cout << "Opcao invalida!" << endl;
        }
    } while (usuario != 0);

    return 0;
}