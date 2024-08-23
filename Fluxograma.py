numero = int(input("Qual o numero?"))

def verificacaoEntrada(numero):
    if numero > 0:
        return "Numero maior que 0"
    elif numero < 0:
        return "Numero menor que 0"
    else:
        return "Igual a 0"
verificacaoEntrada(numero)
print(verificacaoEntrada(numero))