from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('-=' * 13)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 13)
if computador == 0: #PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #PAPEL
    if jogador == 0: #PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #TESOURA
    if jogador == 0: #PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: #TESOURA
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
