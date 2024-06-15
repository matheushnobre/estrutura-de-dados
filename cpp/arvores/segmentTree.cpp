#include <bits/stdc++.h>
using namespace std;

#define MAX 100100

int segmento[MAX*2+1];
int vetor[MAX];

// Demos um nome genérico, mas aqui será a função que for necessária para resolver determinado problema
// Exemplos: retornar o valor mínimo ou máximo, o produto, a soma...
int funcao(int esq, int dir){
    return esq + dir;
}

void criar(int tamanho){
    for(int i = tamanho; i < tamanho*2; i++)
		segmento[i] = vetor[i-tamanho];

	for(int i = tamanho-1; i > 0; i--)
		segmento[i] = funcao(segmento[2*i],segmento[2*i+1]);
}

void atualizar(int i, int valor, int n){ 
	i += n;
    segmento[i] = valor;

	while (i > 1){
		i /= 2;
		int novoValor = funcao(segmento[2*i], segmento[2*i+1]);
			
		if (segmento[i] != novoValor)
			segmento[i] = novoValor;
		else
			break;	
	}	
}

int executar(int inicio, int fim, int n){
	inicio += n;
	fim += n;
	int soma = 0;

	while (inicio < fim){
		if (inicio % 2 == 1){
			soma = funcao(soma, segmento[inicio]);
			inicio++;
		}
		
		if(fim % 2 == 1){
			fim--;
			soma = funcao(soma, segmento[fim]);
		}

		inicio /= 2;
		fim /= 2;
		
	}
	return soma;
	
}

int main(){
    // Vetor = {0, 2, 4, 6, 8}
    int tamanho = 5;
    for (int i=0; i<tamanho; i++){
        vetor[i] = i*2;
    }
    criar(tamanho);

    int opcao;
    do{
        cout<<"\n0. Parar programa\n1. Atualizar vetor\n2. Consultar soma de um intervalo\nSelecione uma opcao: ";
        cin >> opcao;
        if(opcao == 1){
            int indice, valor;
            cout<<"Insira o indice do elemento que deseja atualizar: ";
            cin>>indice;
            cout<<"Insira o novo valor: ";
            cin>>valor;
            atualizar(indice, valor, tamanho);
            cout<<"Vetor atualizado"<<endl;
        } 
        else if(opcao == 2){
            int inicio, fim;
            cout<<"Insira o indice de inicio: ";
            cin>>inicio;
            cout<<"Insira o indice do final: ";
            cin>>fim;
            int soma = executar(inicio, fim, tamanho);
            cout<<"Soma do intervalo = "<<soma<<endl;
        }

    } while(opcao != 0);

    return 0;
}