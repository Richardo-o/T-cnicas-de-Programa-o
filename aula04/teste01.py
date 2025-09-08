#Av Clara Giannoti de Souza, 250, Centro, Registro, SP
vetor = []
frase = 'Av Clara Giannoti de Souza, 250, Centro, Registro, SP'
vetor = frase.split(",")

print(f"A rua é: ",vetor[0])
print(f"O número é: ",vetor[1])

#Outro exemplo

entrada = input("Digite os elementos do vetor separados por espaços: ")

vetor = [int(x) for x in entrada.split()]

print("Vetor: ", vetor)