#include <iostream>
#include "fila.h"

using namespace std;

    queue::queue(){
        first = 0;
        last = 0;
        estrutura = new TipoItem[max_itens];
    }

    queue::~queue(){
        delete[] estrutura;
    }

    bool queue::isEmpty(){
        return (first == last);
    }

    bool queue::isFull(){
        return (last-first == max_itens);
    }

    void queue::push(TipoItem item){
        if (isFull()){
            cout << "A fila esta cheia, logo esse elemento nao pode ser inserido"<<endl;
        } else{
            estrutura[last % max_itens] = item;
            last++;
        }
    }

    TipoItem queue::dequeue(){
        if(isEmpty()){
            cout<<"A fila esta vazia. Nenhum elemento foi removido"<<endl;
            return 0;
        } else{
            first++;
            return estrutura[(first-1) % max_itens];
        }
    }

    void queue::print(){
        cout<<"Fila: [";
        for (int i=first; i<last; i++){
            cout<<estrutura[i%max_itens]<<" ";
        }
        cout<<"]"<<endl;
    }