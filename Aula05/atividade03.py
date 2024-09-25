import os 

os.system ('cls')


print ("\n[1] Adicionar Item \n[2] Remover Item  \n[3] Listar Itens \n[4] Sair : \n")

opcao = int(input("Escolha as opções: "))
valor = 50

match opcao:
    case 1:
        print('Adicionar Item ') 
        adc = int(input('Quantos itens deseja adicionar? '))
        va = valor + adc
        print(f'O valor total é de {va} itens adicionados')
    case 2:
        print('Remover item ') 
        sub = int(input('Quantos itens deseja remover? '))
        sb = valor - sub
        print(f'O valor total é {sb}')
    case 3:
        print(f'Total de itens adicionados {valor}')
    case 4:
        print('Sair')





