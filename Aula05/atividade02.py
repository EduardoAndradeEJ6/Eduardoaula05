import os 

os.system ('cls')

print ("\n[1] Restaurante Chinês \n[2] Restaurante Italiano  \n[3] Restaurante Mexicano \n[4] Restaurante Vegetariano  : \n")


opcao = int(input("Resposta: "))

match opcao:
    case 1:
        print('Prato Chinês')
    case 2:
        print('Prato Italiano')
    case 3:
        print('Prato Mexicano')
    case 4:
        print('Prato Vegetariano')