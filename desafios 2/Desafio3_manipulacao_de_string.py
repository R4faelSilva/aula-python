def manipularString(texto):

    textoMaiusculo = texto.upper()
    textoMinusculo = texto.lower()
    totaisCaracteres = len(texto)

    return (textoMaiusculo, textoMinusculo, totaisCaracteres)
def main()
    palavra = input("Qual é a palavra? ")

    resultadoMaiusculo, resultadoMinusculo, resultadoTotaisCaracteres = manipularString(palavra)

    print(f"Sua palavra em maiusculo: {resultadoMaiusculo}")
    print(f"Sua palavra em maiusculo: {resultadoMinusculo}")
    print(f"Sua palavra em maiusculo: {resultadoTotaisCaracteres}")

main()
# def stringMaiuscula(string):
#     return string.upper()
# def stringMinuscula(string):
#     return string.lower()
# def stringLetras(string):
#     return len(string)
# def main():
#     string = input("Qual a sua string? ")
#     print(f"{stringMaiuscula(string)}, {stringMinuscula(string)}, {stringLetras(string)}")
# main()