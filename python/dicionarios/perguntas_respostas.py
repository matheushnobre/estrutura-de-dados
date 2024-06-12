perguntas = [

    {
        'Pergunta': 'Qual jogador do Flamengo veste a camisa 10?',
        'Alternativas': ['Gabi', 'Arrascaeta', 'Cebolinha', 'Tite', 'Diego'],
        'Resposta': 'Gabi'
    },
    {
        'Pergunta': 'Quem fez o 2º gol do Palmeiras na final da Libertadores de 2021?',
        'Alternativas': ['Rony', 'Breno Lopes', 'Weverton', 'Deyverson', 'Andreas Pereira'],
        'Resposta': 'Andreas Pereira'
    },
    {
        'Pergunta': 'Qual foi o 1º adversário do Flamengo em 2024?',
        'Alternativas': ['Madureira', 'Philadelphia', 'Audax-RJ', 'Nova Iguaçu', 'Orlando City'],
        'Resposta': 'Audax-RJ'
    }
]

def validar_resposta(pergunta, resposta):
    if resposta.isdigit():
        for index, alternativa in enumerate(pergunta['Alternativas']):
            if alternativa == pergunta['Resposta']:
                index_correto = index
                break
        return True if resposta == str(index_correto+1) else False
    else:
        return True if resposta.lower() == pergunta['Resposta'].lower() else False

def main():
    acertos = 0
    print("\nBem-vindo ao sistema de perguntas e respostas do Python!\n")

    for index, pergunta in enumerate(perguntas):
        print("Pergunta #{}: {}".format(index+1, pergunta['Pergunta']))
    
        for index, alternativa in enumerate(pergunta['Alternativas']):
            print(index+1, alternativa, sep=') ')
    
        resposta = input("Escolha uma opção: ")
        if validar_resposta(pergunta, resposta):
            print("Parabéns! Você acertou!")
            acertos += 1
        else:
            print("Infelizmente você errou!")
        
        print(45*'-')
    
    print("Fim de jogo! Você acertou {} resposta(s)".format(acertos))
    
main()