from time import sleep
from operadores import divisao, multiplicacao, adcao, subtracao

print('-='*20)
print('{:^40}'.format("Calcluadora simples"))
print('-='*20)

while True:
    n1 = int(input("Escolha um numero: "))
    n2 = int(input("Escolha outro numero: "))
    operacao = str(input('Escolha uma operação matematica: ')).strip()[0]

    print("calculando...")
    sleep(3)

    if operacao == '/':
        if n2 <= 0:
            print("Conta invalida!")
        if n2 > 0:
            divisao = divisao(n1, n2)
            print(divisao)

    if operacao == '*':
        multiplicacao = multiplicacao(n1, n2)
        print(multiplicacao)
    if operacao == '-':
        subtracao = subtracao(n1, n2)
        print(subtracao)
    if operacao == '+':
        adcao = adcao(n1, n2)
        print(adcao)
    if operacao not in '+-/*':
        print("Escolha uma operação!!")

    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

    if continuar == 'N':
        break
    if continuar not in "SN":
        print("Escolha uma operação valida!")

print("fim do programa!!")
