# 1 - Ler um número inteiro e mostrar o quadrado
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
print("O quadrado de", numero, "é", quadrado)

# 2 - Concatenar primeiro nome e sobrenome
primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = primeiro_nome + " " + sobrenome
print("Seu nome completo é:", nome_completo)

# 3 - Concatenar dois números como strings
num1 = input("Digite o primeiro número inteiro: ")
num2 = input("Digite o segundo número inteiro: ")
concat_str = num1 + num2
print("Concatenação dos números como strings:", concat_str)

# 4 - Concatenar a palavra "Python" com um número inteiro
palavra = "Python"
numero_final = 3  # pode ser qualquer número
resultado = palavra + str(numero_final)
print("Resultado da concatenação:", resultado)

# 5 - Concatenar uma palavra digitada pelo usuário no final de uma frase
frase = "Programar em Python é divertido"
palavra_usuario = input("Digite uma palavra para adicionar à frase: ")
frase_final = frase + " " + palavra_usuario
print("Frase final:", frase_final)