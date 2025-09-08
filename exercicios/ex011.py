#Produto 

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do preço: "))
qtd = int(input("Digite a quantidade: "))

valor = preco*qtd

print(f"O valor total do produto {nome} com  preço R${preco} o valor a ser pago é: R${valor}")