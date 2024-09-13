def saudacao(nome):
    """
    Função que sauda a pessoa\n
    Input: Nome da pessoa\n
    output: saudação
    """
    print(f"Olá {nome}")
nomePessoa = "Rafael"
saudacao(nomePessoa)

def calcular(numero1, numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2

    return (soma, subtracao)

numero1 = float(input("Qual o 1° numero? "))
numero2 = float(input("Qual o 2° numero? "))

valorSoma, valorSubtracao = calcular(numero1, numero2)
print(f"Calor da soma {numero1} + {numero2} = {valorSoma}")
print(f"Calor da subtração {numero1} - {numero2} = {valorSubtracao}")