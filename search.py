from collections import deque


def dfs(node):

    if node is None:
        return

    if node.question:
        print("Pergunta:", node.question)
    else:
        print("Resposta:", node.answer)

    dfs(node.yes)
    dfs(node.no)


def bfs(root):

    queue = deque([root])

    while queue:

        node = queue.popleft()

        if node.question:
            print("Pergunta:", node.question)
        else:
            print("Resposta:", node.answer)

        if node.yes:
            queue.append(node.yes)

        if node.no:
            queue.append(node.no)
