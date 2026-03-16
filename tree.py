class Node:
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None


def create_tree():

    root = Node(question="É um animal?")

    root.yes = Node(question="Vive na água?")
    root.no = Node(question="É um objeto?")

    root.yes.yes = Node(answer="Golfinho")
    root.yes.no = Node(answer="Cachorro")

    root.no.yes = Node(answer="Celular")
    root.no.no = Node(answer="Pedra")

    return root
