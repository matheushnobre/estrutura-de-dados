#include <iostream>
#include "pilha.h"

using namespace std;

    stack::stack(){
        size = 0;
        estrutura = new TipoItem[max_itens];
    }

    stack::~stack(){
        delete estrutura;
    }

    bool stack::isFull(){
        return (size == max_itens);
    }

    bool stack::isEmpty(){
        return (size == 0);
    }

    void stack::push(TipoItem item){
        if (isFull()){
            cout << "A pilha esta cheia, logo nao eh possivel inserir este elemento."<<endl;
        } else{
            estrutura[size] = item;
            size++;
        }
    }

    TipoItem stack::pop(){
        if (isEmpty()){
            cout << "A pilha esta vazia, logo existe elemento para ser removido."<<endl;
            return -1;
        } else{
            size--;
            return estrutura[size];
        }
    }

    void stack::print(){
        cout<<"Pilha [";
        for(int i=0; i<size; i++){
            cout<<estrutura[i]<<" ";
        }
        cout<<"]"<<endl;
    }

    int stack::lenght(){
        return size;
    }