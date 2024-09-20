#range
for a in range(6):
    print(a)
#continue
for i in range(6):
    if i % 2 == 0:
        continue # Pula a interação se i for par

    print("impar: ", i)

#enumerate
listaFrutas = ["Morango", "Uva", "Manga"]

for b, valor in enumerate(listaFrutas):
    print(f"Índice {b}: {valor}")