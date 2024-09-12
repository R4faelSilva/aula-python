texto = input("Qual seu nome completo? ")
sobrenome = texto.split()
ultimoNome = (len(texto))
if ultimoNome > 1: 
    print(sobrenome[-1])
else:
    print("Coloque seu nome completo por favor")