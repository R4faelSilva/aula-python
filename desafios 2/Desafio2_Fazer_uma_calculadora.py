tipoOperacao = ["*", "/", "-", "+"]
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b

def main():
    a = float(input(f"valor A: "))
    b = float(input(f"valor B: "))
    operacao = input("Qual o tipo de operação? (*,/,-,+) ")

    if operacao not in tipoOperacao:
        print("Não existe essa operação")
    if operacao.upper() == "*":
        print(f"A multiplicação é {multiplicacao(a, b)}")
    if operacao.upper() == "/":
        if ({a} or {b} == 0):
            print("Não é possível dividir por zero!")
        else:
            print(f"A divisão é {divisao(a, b)}")
    if operacao.upper() == "-":
        print(f"A subtração é {subtracao(a, b)}")
    if operacao.upper() == "+":
        print(f"A soma é {soma(a, b)}")
main()
