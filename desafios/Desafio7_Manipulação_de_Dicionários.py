alunos = {"Rafael": 8, "Galvão": 10, "Guilherme": 8, "Ryan": 7, "Vinicius": 9.5}
nome = input("Qual o aluno que você deseja saber a nota? ")
if nome in alunos:
    if nome == "Rafael":
        print("A nota é ", (alunos["Rafael"]))
    if nome == "Galvão":
        print("A nota é ", (alunos["Galvão"]))
    if nome == "Guilherme":
        print("A nota é ", (alunos["Guilherme"]))
    if nome == "Ryan":
        print("A nota é ", (alunos["Ryan"]))
    if nome == "Vinicius":
        print("A nota é ", (alunos["Vinicius"]))
else:
    print("O aluno não esta no banco de dados.")