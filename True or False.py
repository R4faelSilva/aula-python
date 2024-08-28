a = 2
b = 6
c = 3

operacaoAnd = a == b and c * a == b
print(f"Operação And 1 {operacaoAnd}")
operacaoOr = a == b or c * a == b
print(f"Operação Or 1 {operacaoOr}")
print(operacaoOr)
print("###########################")

operacaoAnd = a == (c + b) and b == c
print(f"Operação And 2 {operacaoAnd}")
print(operacaoAnd)
operacaoOr = a == (c + b) or b == c
print(f"Operação Or 2 {operacaoOr}")
print(operacaoOr)
print("###########################")

operacaoAnd = a > 5 and b > 3
print(f"Operação And 3 {operacaoAnd}")
print(operacaoAnd)
operacaoOr = a > 5 or b > 3
print(f"Operação Or 3 {operacaoOr}")
print(operacaoOr)
print("###########################")

operacaoAnd = a < 5 and c >= 3
print(f"Operação And 4 {operacaoAnd}")
print(operacaoAnd)
operacaoOr = a < 5 or c >= 3
print(f"Operação Or 4 {operacaoOr}")
print(operacaoOr)
print("###########################")

operacaoAnd = not b == 6 and 3 * 2 == b
print(f"Operação And 5 {operacaoAnd}")
print(operacaoAnd)
operacaoOr = not b == 6 or 3 * 2 == b
print(f"Operação Or 5 {operacaoOr}")
print(operacaoOr)
print("###########################")

operacaoAnd = c < 5 and not b > 6
print(f"Operação And 6 {operacaoAnd}")
print(operacaoAnd)
operacaoOr = c < 5 or not b> 6
print(f"Operação Or 6 {operacaoOr}")
print(operacaoOr)
print("###########################")