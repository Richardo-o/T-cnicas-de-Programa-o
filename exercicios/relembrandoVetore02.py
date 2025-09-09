matriz = []
maioresquedez = 0

# MATRIZ 4X4
for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        numero = int(input(f"Digite um valor inteiro na posição {i+1},{j+1}: "))
        linha.append(numero)
        if numero > 10:
            maioresquedez += 1

print(matriz)
print(f"Existem {maioresquedez} números maiores que 10.")
