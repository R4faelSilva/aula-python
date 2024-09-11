# Abrir arquivo

with open("teste.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read() # Tem q colocar .read dps de definir a variável do arquivo para então fazer a variável conteudo
    print(conteudo) 

# Escrever arquivo

with open("teste2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá Mundo!\n")
    arquivo.write("aaaaaaaaaaaaaaaaaaaaaaaaaaa")

# Acrescentar

with open("teste.txt", "a", encoding="utf=8") as arquivo:
    arquivo.write("\nTesto adicional") # \n manda para a linha de baixo