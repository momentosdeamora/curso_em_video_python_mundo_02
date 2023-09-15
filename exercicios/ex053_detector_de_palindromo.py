frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa as palavras em um vetor / faz uma lista
junto = ''.join(palavras) #juntou tudo em uma string
'''inverso = '' '''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1): #Fez o enverso dela: foi na última letra até a primeira voltando uma letra
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
    