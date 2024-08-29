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