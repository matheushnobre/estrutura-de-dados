#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool isValid(string expressao){
    stack<char> pilha;
    for(char c : expressao){
        if (c=='(') pilha.push('(');
        else if (c==')'){
            if (pilha.empty()) return false;
            else pilha.pop();
        }
    }

    if (pilha.empty()) return true;
    else return false;
}

int main(){
    string expressao;
    while(getline(cin, expressao)){
        if(isValid(expressao)) cout<<"correct"<<endl;
        else cout<<"incorrect"<<endl;
    }
    return 0;
}