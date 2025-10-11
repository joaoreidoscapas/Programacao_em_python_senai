# Exercício 0
lista = list(range(2, 21, 2))
print("Exercício 0:", lista)

# Exercício 1
numeros = list(range(1, 11))
print("Exercício 1:", numeros)

# Exercício 2
print("Exercício 2:", numeros[2])  # terceiro elemento (índice 2)

# Exercício 3
numeros.append(9)
print("Exercício 3:", numeros)

# Exercício 4
numeros.remove(5)
print("Exercício 4:", numeros)

# Exercício 5
carros = ['tesla', 'ferrari', 'Jeep']
print("Carros:", carros)
print("Números:", numeros)

carros += numeros  # concatena a lista numeros no final da lista carros
print("Exercício 5:", carros)