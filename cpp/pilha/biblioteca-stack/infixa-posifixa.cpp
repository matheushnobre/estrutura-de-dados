#include <iostream>
#include <string>
#include <map>
#include <stack>

using namespace std;

map<char, int> operadores = {{'^', 6}, {'*', 5}, {'/', 5}, {'+', 4}, {'-', 4}, {'>', 3}, {'<', 3}, {'=', 3}, {'#', 3}, {'.', 2}, {'|', 1}};
string operandos = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789";

bool isOperando(char c){
    for (char o : operandos){
        if (c == o){
            return true;
        }
    }
    return false;
}

int isValid(string exp){
    stack<char> parenteses;
    bool isOperador = false;

    if (operadores.count(exp[0])==1 || operadores.count(exp[exp.size()-1])==1){
        return 1;
    }

    for (char c : exp){
        if(operadores.count(c) == 1){
            if (isOperador){
                return 1; //Syntax Error
            } else{
                isOperador = true;
            }
        } else{
            isOperador = false;
        }
        
        if (c=='('){
            parenteses.push('(');
        } else if(c==')'){
            if(parenteses.empty()){
                return 1; //Syntax Error
            }
            parenteses.pop();
        } else if (!isOperando(c) && operadores.count(c) != 1){
            return 2; // Lexical Error
        }
    }
    if (!parenteses.empty()){
        return 1; // Syntax Error
    }
    return 0; //É válido
}

string converterPosfixa(string exp){
    stack<char> oper;
    string posf = "";

    for (char c : exp){
        if (isOperando(c)){
            posf += c;
        } else if(c == '('){
            oper.push('(');
        } else if(c == ')'){
            char item = oper.top();
            oper.pop();
            while (item != '('){
                posf += item;
                item = oper.top();
                oper.pop();
            }
        } else{
            while (!oper.empty() && oper.top()!='('){
                if (operadores[oper.top()] >= operadores[c]){
                    posf += oper.top();
                    oper.pop();
                } else{
                    break;
                }
            }
            oper.push(c);
        }
    }

    while (!oper.empty()){
        posf += oper.top();
        oper.pop();
    }

    return posf;
}

int main(){
    string exp;
    string posf;

    while (getline(cin, exp)){
        int valid = isValid(exp);
        if(valid == 1){
            cout<<"Syntax Error!"<<endl;
        } else if(valid == 2){
            cout<<"Lexical Error!"<<endl;
        } else{
            cout<<converterPosfixa(exp)<<endl;
        }
    }


    return 0;
}