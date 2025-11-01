# Cadastro de clientes
clientes = []

# Tipos de quartos e preços
quartos = {"Simples": 100, "Duplo": 150, "Luxo": 250}

# Cadastro e reserva de 3 clientes
for i in range(1, 4):
    nome = input(f"Digite o nome do Cliente {i}: ")
    idade = int(input(f"Digite a idade do Cliente {i}: "))
    clientes.append({"nome": nome, "idade": idade})

    quarto = input(f"{nome}, escolha seu quarto (Simples/Duplo/Luxo): ").strip().capitalize()
    dias = int(input(f"{nome}, quantos dias ficará no hotel? "))

    total = quartos.get(quarto, 0)
    if total == 0:
        print(f"Quarto inválido para {nome}!")
    total *= dias

    clientes[-1].update({"quarto": quarto, "dias": dias, "total": total})

# Exibir valores a pagar
print("\n=== RESUMO DAS RESERVAS ===")
for cliente in clientes:
    print(f"{cliente['nome']}: Quarto {cliente['quarto']}, {cliente['dias']} dias, Total a pagar: R$ {cliente['total']},00")