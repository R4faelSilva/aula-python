# Variaveis de Preço
precosProdutos = [100,200,100] # coloca os preços em uma lista
precoTotal = sum(precosProdutos) # para depois somar todos e dar o valor total
valDesconto = 0

if precoTotal > 500:
    valDesconto = precoTotal * 0.1 # multiploca o valor totla pelo desconto para dar o valor com o desconto
    valFinal = int(precoTotal - valDesconto) # pega o valor com desconto e subtrai do total
    print(f"Total com desconto R$: {valFinal}")
    
else:
    print(f"Adicione mais itens para um desconto de 10%")

# printa a descrição com as variáveis que eu redefini 
print(f"Total R$: {precoTotal}")