from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opcao = int(input('\n>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('\nA soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('\nO resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('\nEntre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('\nInforme os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\nFinalizando... ')
        sleep(2)
    else:
        print('\nOpção inválida. Tente novamente.')
    print('=-=' * 10)
print('\nFim do programa! Volte sempre!')
