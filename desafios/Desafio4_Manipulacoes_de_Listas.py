frutas = ["Morango", "Jumanji", "Astralopitécus"]
print("Lista de 'frutas': ", frutas)
frutas.append("Jabuticaba")
print("Lista de 'frutas' atualizada: ", frutas)

removerFrutas = input("Qual fruta você quer remover? ")
if removerFrutas in frutas:
    frutas.remove(removerFrutas)
    print("Nova lsta de frutíferos: ", frutas)