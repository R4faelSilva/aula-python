# Variaveis de Preço
precosProdutos = [100,200,300] # coloca os preços em uma lista
precoTotal = sum(precosProdutos) # para depois somar todos e dar o valor total
valDesconto = 0

if precoTotal > 500:
    valDesconto = precoTotal * 0.1 # multiploca o valor totla pelo desconto para dar o valor com o desconto
    
else:
    print(f"Adicione mais itens para um desconto de 10%")

valFinal = int(precoTotal - valDesconto) # pega o valor com desconto e subtrai do total

# printa a descrição com as variáveis que eu redefini
print(f"Total antes do desconto: {precoTotal}") 
print(f"Total com desconto: {valFinal}")

