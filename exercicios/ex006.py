salario = float(input("Digite o valor do seu salario: "))
percentual = float(input("Digite o valor da porcentagem do reajuste: "))

percentual = percentual/100

reajuste = salario * percentual

print(f"Seu novo salario será: {reajuste + salario} ")