# Variaveis de Preço
preços = [100,200,300] # coloca os preços em uma lista
total = sum(preços) # para depois somar todos e dar o valor total

desconto = 0
multiplicadorDesconto = 0.1

if total > 500: # se o valor total passar de 500 ele aplica um certo desconto
    valDesconto = total * multiplicadorDesconto # multiploca o valor totla pelo desconto para dar o valor com o desconto

valFinal = total - valDesconto # pega o valor com desconto e subtrai do total

# printa a descrição com as variáveis que eu redefini
print(f"Total antes do desconto: {total}") 
print(f"Desconto aplicado: {desconto}")
print(f"Total com desconto: {valFinal}")