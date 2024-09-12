notas = {"Rafael": 8, "Galvão": 10, "Guilherme": 8, "Ryan": 7, "Vinicius": 9.5}
nome = input("Qual o aluno que você deseja saber a nota? ")
if nome in notas:
    if nome in notas:
        print(f"A nota de {nome} é {notas[nome]}.")
else:
    print("O aluno não esta no banco de dados.")