'''for c in range(0,6): #Dentro e Fora do Laço
    print('Oi')
print('Fim')'''

'''for c in range(1,6): #Ele ignora o último
    print(c)
print('Fim')'''

'''for c in range(6, 0): #Ele não conta
    print(c)
print('Fim')'''

'''for c in range(6, 0, -1): #Ele conta para trás
    print(c)
print('Fim')'''

'''for c in range(0, 7, 2): #Ele pula de 2 em 2
    print(c)
print('Fim')'''

''' n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')'''

'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

'''for c in range(0, 3):
    n =int(input('Digite um valor: '))
print('Fim')'''

s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
