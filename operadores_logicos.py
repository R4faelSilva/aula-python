diaMaximo = 28
idadeMinima = 14
idadeMaxima = 17
verf = True

dia = int(input("Que dia é hoje?"))
idade = int(input("Qual a idade?"))
listaEspera = input("Está na lista de espera?")
indicacao = input("Tem indicação?")

if (dia <= diaMaximo == True) or (indicacao == "Sim" and dia == 29):
    if (idade >= idadeMinima) or (idade <= idadeMaxima):
        if not listaEspera == "sim":
            print("Inscrição realizada\n")
if listaEspera == "Sim":
    print("A inscrição não pode ser realizada\n")
    verf = False
if idade < idadeMinima:
    print("Você não tem a idade necessária\n")
    verf = False
if idade > idadeMaxima:
    print("Possui mais do que a idade indicada\n")
    verf = False
if (dia > 28) and (indicacao == "Não"):
    print("A data de inscrição expirou\n")
    verf = False
if verf == False:
    print("Sua incrição foi negada!\n")