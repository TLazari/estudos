# faça fatorial de um número

val = int(input("Digite um número: "))
fat = 1
for i in range(1, val+1):
    fat *= i
print(f"O fatorial de {val} é {fat}")
