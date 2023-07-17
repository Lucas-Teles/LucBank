import os
os.system('cls')
saldo = 0
extrato = ""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

boas_vindas = f"""
Olá !
Você está acessando o app da LucBank
Que ação deseja realizar:
"""
menu = """
        [0] - Depositar
        [1] - Sacar
        [2] - Extrato
        [3] - Sair

"""


print(boas_vindas)
while True:
    # MENU INICIAL
    opcao = input(f'{menu} > ')
    print('')
    if opcao == "0":    
        valor = float(input("Quanto deseja depositar? [Ex: 50.50] \n"))
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso !")
            extrato += f'Depósito de R$ {valor:.2f}\n'
        else:
            print("Valor inserido inválido")


    elif opcao == "1":
        while numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                saque = float(input("Quanto deseja sacar. Max de saque -> R$ 500: \n"))
                if saque > saldo:
                    print("> Saldo insuficiente <")
                    break
                else:
                    if saque <= LIMITE and saque > 0:
                        print("Saque realizado com sucesso !")
                        saldo -= saque
                        numero_saques +=1
                        extrato += f'Realizado saque de R$ {saque:.2f}\n'
                        break
                    elif saque > LIMITE:
                        print("Valor inserido maior que o permitido")
                    else:
                        print("valor inválido, tente novamente\n")
            else:
                print("Saldo insuficiente")
                break


    elif opcao == "2":
        print("======  E X T R A T O  ======\n")
        print(extrato)
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
        print("\n======  L U C B A N K  ======")
    elif opcao == "3":
        print("Obrigado !, volte sempre")
        break
    else:
        print("opção inválida tente novamente")
    
    novamente = input("\n> Deseja realizar outra ação ? (s/n):<  \n")
    if novamente == "s":
        print('O que deseja fazer:  ')
    elif novamente == "n":
        print('Obrigado pela preferencia, volte sempre !')
        break
    else:
        print('INVALIDO. ATÉ A PROXIMA')
        break
    os.system('cls')        
