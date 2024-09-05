idade = int(input("Qual a idade?: ")) # Colocar a idade como input para ser possível adicionar qualquer valor

categoria = "Indefinida"

# No trecho de condição será validada a idade da persona para analisar sua categoria
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

# professor (fez com def)
def validarIdade(idade):
    mensagemPadrao = "A pessoa é classificada como: "
    if idade < 0:
        return "Essa pessoa ja nasceu????"
    elif idade > 0 and idade <= 2:
        return  mensagemPadrao + "Bebê"
    elif idade > 2 and idade <= 13:
        return mensagemPadrao + "Criança"
    elif idade >= 13 and idade < 18:
        return mensagemPadrao + "Adolescente"
    elif idade >= 18 and idade < 60:
        return mensagemPadrao + "Adulto(a)"
    elif idade > 106:
        print("Para de mentir '-'")
    else:
        return "Idoso"
# Chamar a variável do def para dar um valor à variável do print 
categoriaIdade = validarIdade(idade)
# Usa a variável no print deinida pelo def 
#print(f"A pessoa é classificada como: {categoriaIdade}")
print(categoriaIdade)