
numeros = []

for i in range(5):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
numeros.sort()

print("Los números ordenados de menor a mayor son:")
for numero in numeros:
    print(numero)
