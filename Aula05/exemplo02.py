import os 

os.system ('cls')



# idade = int(input('Informe a sua idade: '))

# match idade:
#     case i if i <12:
#         print('Você é uma criança. ')
#     case i if 12<= i <18:
#         print('Você é uma adolescente.')
#     case i if i >18:
#         print("Você é um adulto. ")
#     case _:
#         print('Idade inválida')



print(30*'=')

turno = int(input ('Informe o número do turno: '))

match turno:
    case 1:
        print('Manhã')
    case 2:
        print ('Tarde')
    case 3:
        print ('Noite')
    case _:
        print('Turno inválido')