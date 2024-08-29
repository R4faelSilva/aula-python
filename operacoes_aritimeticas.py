a = 7
b = 3

# Adição (+)
resultado = a + b
print("###########################")
print("  ")
print(f"Soma: {resultado}")

# Subtração (-)
resultado = a - b
print(f"Subtrração: {resultado}")

# Multiplicação (*)
resultado = a * b
print(f"Multiplicação: {resultado}")

# Divisão (/)
resultado = a / b
print(f"Divisão: {resultado}")

# Divisão Inteira (//)
resultado = a // b
print(f"Divisão Inteira: {resultado}")

# Resto da divisão (%)
resultado = a % b
print(f"Resto da divisão: {resultado}")

# Expoente (**)
resultado = a ** b
print(f"Expoente: {resultado}")
print("  ")
print("###########################")

saldoInicial = 50
custoRefri = 8
custoPao = 4
morta = 39.90

valorCompra = (custoRefri * 2) + custoPao + ((morta / 1000) * 300) # ou morta * 0.3

saldoFinal = saldoInicial - valorCompra
print("  ")
print(f"José chegou com R${saldoInicial} e saiu com R${saldoFinal}")
print("  ")

dia = int(input ("Qual o dia de hoje?"))
pedidoFreddy = int(input ("Quantas pizzas foram compradas?"))
pedidoBebida = int(input ("Quantas bebidas foram compradas?"))
pedidoBolo = int(input ("Quantas bolo foram compradas?"))
pedidoDoce = int(input ("Quantas doce foram compradas?"))
print("###########################\n")

diaFesta = 26
freddymin = 10
bebidasmin = 12
bolomin = 5
docemin = 600 

if diaFesta == dia:
    print("Ana esta fazendo compras no dia da festa!\n")
else:
    print("Nem é o dia da festa\n")
print("###########################\n")
if (freddymin > pedidoFreddy):
    print("Ana não comprou o suficiente na Freddy's Pizzaria\n")
else:
    print("A Ana teve coragem de comprar na Freddy's\n")
print("###########################\n")
if (bebidasmin > pedidoBebida):
    print("Ana não comprou bebidas o suficiente!\n")
else:
    print("A Ana comprou bebidas o suficiente\n")
print("###########################\n")
if (bolomin > pedidoBolo):
    print("Ana não comprou bolos o suficiente!\n")
else:
    print("A Ana comprou bolos o suficientes embora seja muitos\n")
print("###########################\n")
if (docemin > pedidoDoce):
    print("Ana não comprou gramas de doces o suficiente!\n")
else:
    print("A Ana comprou as gramas correta de doces\n")
print("###########################\n")
print("Ana esqueceu do Golden Freddy na lojinha de lembranças da Freddy's\n")
