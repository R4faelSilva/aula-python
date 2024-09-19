notas = {"Rafael": 8, "Galvão": 10, "Guilherme": 8, "Ryan": 7, "Vinicius": 9.5}

def recuperarNotaAluno(nome):
    try:
        if nome in notas:
            print(f"A nota de {nome} é {notas[nome]}.")
        else:
            raise KeyError
    except KeyError:
        print("O aluno não esta no banco de dados.")

        operacao = input("Deseja tentar novametne (S/N)? ")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa encerrado.")
        else:
            raise ValueError("Operação não reconhecida")
        print("O programa irá finalizar.")
def main():
    try:
        nome = input("Qual o aluno que você deseja saber a nota? ")
        recuperarNotaAluno(nome)
    except Exception as e:
        print(f"Ocorreu um erro {e}")
main()