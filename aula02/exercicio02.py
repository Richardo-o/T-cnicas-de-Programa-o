n = int (input("Digite um numero inteiro: "))

if n%2==0:
    print("O numero é par")
    resultado = n**2
    print(f"O cubo de {n} é:{resultado}")
else: 
    print("O numero é ímpar")
    resultado = n**3
    print(f"O cubo de {n} é:{resultado}")