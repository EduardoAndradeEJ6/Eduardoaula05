import os 

os.system ('cls')


print(30*'=')

n = int(input("Informe um número entre 1 e 12: "))


match n:
    case i if i == 1:
        print('Mês de Janeiro')
    case i if i == 2:
        print('Mês de Fevereiro')
    case i if i == 3:
        print('Mês de Março')
    case i if i == 4:
        print('Mês de Abril')
    case i if i == 5:
        print('Mês de Maio')
    case i if i == 6:
        print('Mês de Junho')
    case i if i == 7:
        print('Mês de Julho')
    case i if i == 8:
        print('Mês de Agosto')
    case i if i == 9:
        print('Mês de Setembro')
    case i if i == 10:
        print('Mês de Outubro')
    case i if i == 11:
        print('Mês de Novembro')
    case i if i == 12:
        print('Mês de Dezembro')
    case i if i > 12:
        print('Número inválido, digite entre 1 e 12!')