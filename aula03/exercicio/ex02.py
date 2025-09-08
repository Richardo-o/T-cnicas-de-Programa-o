indice = int(input("Digite o indice de poluição"))

match indice:
    case 0 | 1 | 2:
        print("Indice de poluição considerado aceitavel!")
    case 3 | 4 | 5:
        print("Indice de poluição alto, suspender atividades em Grupo!")
    case 6 | 7 :
        print("Indice de poluição alto, suspender atividades em Grupo!")   
    case _:
        print("Indice de poluição alto, suspender atividades em Grupo!") 