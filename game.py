def jogar(root):

    node = root

    while node.answer is None:

        resposta = input(node.question + " (s/n): ").lower()

        if resposta == "s":
            node = node.yes
        else:
            node = node.no

    print("\nVocê pensou em:", node.answer)
