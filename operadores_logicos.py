diaMaximo = 28
idadeMinima = 14
idadeMaxima = 17
verf = True

dia = int(input("Que dia é hoje?"))
idade = int(input("Qual a idade?"))
listaEspera = int(input("Está na lista de espera?"))
indicacao = int(input("Tem indicação?"))

if (dia <= diaMaximo == True) or (indicacao.upper() == "sim" and dia == 29):
    if (idade >= idadeMinima) or (idade <= idadeMaxima):
        if not listaEspera == "sim":
            print("Inscrição realizada")
if listaEspera == "Sim":
    print("A inscrição não pode ser realizada")
    verf = False
if idade < idadeMinima:
    print("Você não tem a idade necessária")
    verf = False
if idade > idadeMaxima:
    print("Possui mais do que a idade indicada")
    verf = False
if (dia > 28) and (indicacao == "Não"):
    print("A data de inscrição expirou")
    verf = False
if verf == False:
    print("Sua incrição foi negada!\n")