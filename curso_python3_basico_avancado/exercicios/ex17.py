# Exercicios - Sistemas de perguntas e respostas

"""
Crie um sistemas de perguntas e resposta onde o usuario
interaja com o sistema dinamicamente respondendo as perguntas
e o sistema diga se ele acertou ou errou, faça a contagem de quantas voce acertou
ao final do programa.
"""

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    for opcao in pergunta['Opções']:
        print(opcao)
    print()