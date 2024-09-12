tupla = (50, 70, 80)
print(tupla)

# x = int(input("Qual a nova coordenada x? "))
# y = int(input("Qual a nova coordenada y? "))
# z = int(input("Qual a nova coordenada z? "))
# tupla = (x, y, z)
# print(f"X: {tupla[0]} Y: {tupla[1]} Z: {tupla[2]}" )

novoIndice = int(input("Qual a nova coordenada? "))
tupla = (tupla[0], novoIndice, tupla[1])
print(tupla)