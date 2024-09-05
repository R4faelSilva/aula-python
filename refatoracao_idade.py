idade = int(input("Qual a idade?: ")) # Colocar a idade como input para ser possível adicionar qualquer valor

categoria = "Indeinida"
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"A pessoa é classificada como: {categoria}")