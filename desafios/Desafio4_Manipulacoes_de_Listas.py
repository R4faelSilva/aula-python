frutas = ["Morango", "Jumanji", "Astralopitécus"]
print("Lista de 'frutas': ", frutas)
adicionar = input("Qual a nova fruta? ")
frutas.append(adicionar)
print("Lista de 'frutas' atualizada: ", frutas)

removerFrutas = input("Qual fruta você quer remover? ")
if removerFrutas in frutas:
    frutas.remove(removerFrutas)
    print("Nova lsta de frutíferos: ", frutas)