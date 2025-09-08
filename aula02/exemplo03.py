print('## Programa de empréstimos 0-Não e 1-Sim')

negativado = int(input("Possui nome negativado? "))
if negativado == 1:
    print("Não pode realizar empréstimo")

else: 
    possuiCasaPropria = int(input("Você possui casa propria? "))
    if possuiCasaPropria == 1:
       print("Não pode realizar empréstimo")

    else:
        print("Conceder empréstimo")