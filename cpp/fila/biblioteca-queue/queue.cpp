#include <iostream>
#include <queue>

using namespace std;

int main(){
    queue<int> fila;
    int elemento;

    for (int i=0; i<5; i++){
        cout<<"Insira um elemento na fila: ";
        cin>>elemento;
        fila.push(elemento);
    }

    cout<<"\nPrimeiro elemento: "<<fila.front()<<endl;
    cout<<"Ultimo elemento: "<<fila.back()<<endl<<endl;

    while (!fila.empty()){
        cout<<"Elemento removido: "<<fila.front()<<endl;
        fila.pop();
    }

    return 0;
}