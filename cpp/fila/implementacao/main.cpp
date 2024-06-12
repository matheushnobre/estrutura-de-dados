#include <iostream>
#include "fila.h"

using namespace std;

int main(){
    queue fila;
    TipoItem item;
    int opcao;

    cout<<"Programa gerador de fila"<<endl;
    do {
        cout << "Digite 0 para parar o programa"<<endl;
        cout << "Digite 1 para inserir um elemento"<<endl;
        cout << "Digite 2 para remover um elemento"<<endl;
        cout << "Digite 3 para imprimir a fila"<<endl;
        cout << "Opcao desejada: ";
        cin >> opcao;

        if (opcao == 1){
            cout<<"Digite o elemento a ser inserido: ";
            cin>>item;
            fila.push(item);
            cout<<"Elemento inserido"<<endl;
        } else if (opcao == 2){
            item = fila.dequeue();
            if (item != -1){
                cout<<"Elemento removido: "<<item<<endl;
            } 
        } else if(opcao == 3){
            fila.print();
        }
        cout<<endl;

    } while (opcao != 0);
    
    return 0;
}