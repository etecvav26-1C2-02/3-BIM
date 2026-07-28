#include <iostream>
#include <string>

using namespace std;

class Cliente {
    private:
        int idade;
        int altura;
        int peso;
        string nome;
        
    public:
        // Construtor: serve para a gente preencher os dados do cliente na hora de criar ele
        Cliente(string n, int i, int a, int p) {
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
};

int main() {
    int idade;
    int altura;
    int peso;
    string nome;
    
    
    cout << "Sistema de Academia Iniciado!" << endl;
    cout << "Digite o nome do cliente: ";
    cin >> nome;
    cout << "Digite o altura do cliente: ";
    cin >> altura;
    cout << "Digite o peso do cliente: ";
    cin >> peso;
    cout << "Digite o idade do cliente: ";
    cin >> idade;
    Cliente cliente(nome, idade, altura, peso);
    cout << "Dados do cliente: " << endl;
    cout << "Nome do cliente: " << cliente.GetNome() << endl;
    cout << "Idade do cliente: " << cliente.GetIdade() << endl;
    cout << "Nome do cliente: " << cliente.GetAltura() << endl;
    cout << "Nome do cliente: " << cliente.GetPeso() << endl;
    
    return 0;
}
