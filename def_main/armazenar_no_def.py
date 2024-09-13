alunos = {"Rafael": 8, "Galvão": 10, "Guilherme": 8, "Ryan": 7, "Vinicius": 9.5}

def recuperarNotaAluno(aluno):
    if aluno in alunos:
        print(f"O aluno {aluno} esta com nota: {alunos[aluno]}")
    else:
        print("Aluno não encontrado!")

        operacao = input("Deseja tentar novamente? (S/N) ")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa finalizado")
        else:
            print("Operação não reconhecida! O programa será finalizado.")

def main():
    aluno = input("Qual aluno? ")

    recuperarNotaAluno(aluno)

main()