nulo = int(input("Digite o votos nulos: "))
branco = int(input("Digite o numero de votos em brancos: "))
valido = int(input("Digite o numero de votos válidos: "))


total = nulo + branco + valido

percNulo = (nulo*100)/total
percBranco = (branco*100)/total
percValido = (valido*100)/total

print(f"Percentual de nulos: {percNulo}% \n Percentual de brancos: {percBranco}% \n Percentual de válidos: {percValido}% ")