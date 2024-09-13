
def celsiusParafahrenheit(temperatura):
    return (temperatura - 32) * (5/9)
def fahrenheitParaCelsius(temperatura):
    return (temperatura * 1.8) + 32

def main():
    tipoTemperatura = input("Celsius ou Fahrenheit? (C/F) ")
    temperatura = float(input("Qual a temperatura? "))

    if tipoTemperatura.upper() == "C":
        print(f"A temperatura em graus C° é: {(temperatura):.2f} e em F° é: {fahrenheitParaCelsius(temperatura):.2f}")
    if tipoTemperatura.upper() == "F":
        print(f"A temperatura em graus F° é: {(temperatura):.2f} e em C° é: {celsiusParafahrenheit(temperatura):.2f}")
    else:
        print("Não é uma medida de temperatura.")

main()