# Exemplo com lista
frutas = ["maçã", "banana", "laranja"]
print("Lista de frutas: ", frutas)

# Adicionando um item
frutas.append("uva")
print("Lista de frutas atualizada: ", frutas)

# Acessando um item
print("Primeira fruta: ", frutas[0])

# Removendo um iten da lista 
frutas.remove(frutas[2])
print("Lista de frutas atualizada com fruta removida: ", frutas)

# Exemplo com dicionários/objeto
pessoa = {"nome": "Ana", "idade": 30}
print("Pessoa:", pessoa)

# Acessando valores
print("Nome", pessoa["nome"])

# Adicionando um novo par chave-valor
pessoa["cidade"] = "São Paulo"
print("Pessoa atualizada:", pessoa)

# Dicionário dentro do dicionário
pessoa2 = {"nome2": "Brenda", "Idade": 26, "filhos": {"nome2": "Catarina", "idade2": 6}}

print(pessoa2)
print(pessoa2["nome2"])
print(pessoa2["filhos"])
print(pessoa2["filhos"]["nome2"])
del pessoa2["filhos"]
print(pessoa)

# Dicionário dentro do dicionário
# Definição da lista e dicionário
listaPessoas = []

# Adicioando dicionário dentro da variável
pessoa3 = {"nome3": "Ana", "idade3": 32}
listaPessoas.append(pessoa3)
print(listaPessoas)

# Adicioando ouro dicionário dentro da variável
pessoa3 = {"nome3": "Brenda", "idade3": 26}
listaPessoas.append(pessoa3)
print(listaPessoas)

pessoa3 = {"nome3": "Fernanda", "idade3": 48}
listaPessoas.append(pessoa3)
print(listaPessoas)

# Analisando o dicionário de índice 1 da lista
brenda = listaPessoas[1]
print(brenda)

# Tupla x = 10 y = 30 z = 20
tupla = (10, 20)
print(tupla)

tupla = (tupla[0], 30, tupla[1])
print(tupla)

# x = 10 y = 30 z = 20
tupla = (10,20,30)
print(tupla)
novoIndice = 30
tupla = (tupla[0], novoIndice, tupla[1])
print(tupla)

# Conjunto eliminando duplicados
lista = [1, 2, 2, 3, 4, 4]
conjunto = set(lista)
print(conjunto)

# Operações matemáticas de conjunto
a = {1, 2, 3}
b= {3, 4, 5}
print(a & b)
print(a | b) 
print(a - b)

# Verificação de membros
conjunto = {1, 2, 3, 4, 5}
print(3 in conjunto) # True
print(6 in conjunto) # False

# Tipos de dados
variavel = int 
def soma(a: int, b: int) -> int:
    return a + b
# n compreendi essa
