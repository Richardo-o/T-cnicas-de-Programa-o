

opcao = int(input("1.Tensão (em Volt)\n 2.Resistência (em Ohm) \n 3.Corrente (em Ampére)\n Digite: "))
match opcao:
    case 1:
        R = float(input("Digite a Resistencia em Ohm: "))
        i = float(input("Digite a corrente em Ampere: "))
        U = R*i
        print(f"A tensão é: {U}")
    case 2:
        U = float(input("Digite o valor da Tensão em volt: "))
        i = float(input("Digite a corrente em Ampere: "))
        R = U/i
        print(f"A Resistencia é: {R}")
    case 3:
        U = float(input("Digite o valor da Tensão em volt: "))
        R = float(input("Digite a Resistencia em Ohm: "))
        i = U/R
        print(f"A corrente é: {i}")
    case _:
     print("Digite uma das opções")