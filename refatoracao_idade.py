idade = int(input("Qual a idade?: ")) # Colocar a idade como input para ser possível adicionar qualquer valor

categoria = "Indefinida"
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
elif idade > 100:
    print("Para de mentir '-'")
else:
    categoria = "Idoso"

print(f"A pessoa é classificada como: {categoria}")