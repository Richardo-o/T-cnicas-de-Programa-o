#Azulejos na parede

hp = float(input("Digite a altura da parede: "))
bp = float(input("Digite a base da parede: "))

ha = float(input("Digite a altura do azulejo: "))
ba = float(input("Digite a base do azulejo: "))

areaP= (hp*bp)/2
areaA= (ha*ba)/2


result = areaP/areaA

print(f"O resultado é {result}")