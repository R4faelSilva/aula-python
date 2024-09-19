def main():
    contatos = []

    print(f"A lista atualemnte contem {len(contatos)}")

    pessoaAlice = {"nome": "Alice", "telefone": "123-456-789"}
    pessoaBob = {"nome": "Bob", "telefone": "987-654-321"}

    contatos.append(pessoaAlice)
    print(f"Lista atual: {len(contatos)}")
    print(f"Lista atualizada: {contatos}")

    contatos.append(pessoaBob)
    print(f"Lista atual: {len(contatos)}")
    print(f"Lista atualizada: {contatos}")

main()