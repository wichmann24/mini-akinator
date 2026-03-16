# Mini Sistema de Adivinhação – Exemplo 2 (Frutas)

## Estrutura da Árvore

```
                    É uma fruta?
                   /           \
                Sim             Não
               /                 \
        Tem casca grossa?     É um animal?
          /        \           /       \
      Abacaxi     Banana     Cachorro  Pedra
```

---

# Código Python

```python
from collections import deque

class Node:
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None


# -------- CRIANDO A ÁRVORE --------

root = Node(question="É uma fruta?")

root.yes = Node(question="Tem casca grossa?")
root.no = Node(question="É um animal?")

root.yes.yes = Node(answer="Abacaxi")
root.yes.no = Node(answer="Banana")

root.no.yes = Node(answer="Cachorro")
root.no.no = Node(answer="Pedra")


# -------- DFS --------

def dfs(node):

    if node is None:
        return

    if node.question:
        print("Pergunta:", node.question)
    else:
        print("Resposta:", node.answer)

    dfs(node.yes)
    dfs(node.no)


# -------- BFS --------

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


# -------- JOGO --------

def jogar(root):

    node = root

    while node.answer is None:

        resposta = input(node.question + " (s/n): ").lower()

        if resposta == "s":
            node = node.yes
        else:
            node = node.no

    print("\nVocê pensou em:", node.answer)


# -------- EXECUÇÃO --------

print("\nDFS:")
dfs(root)

print("\nBFS:")
bfs(root)

print("\nJogo de adivinhação")
jogar(root)
```

---

# Ordem de Visita

## DFS

```
É uma fruta?
Tem casca grossa?
Abacaxi
Banana
É um animal?
Cachorro
Pedra
```

---

## BFS

```
É uma fruta?
Tem casca grossa?
É um animal?
Abacaxi
Banana
Cachorro
Pedra
```

---

# Exemplo de Execução do Jogo

```
É uma fruta? (s/n)
> s

Tem casca grossa? (s/n)
> n

Você pensou em: Banana
```

---

# Comparação

**Algoritmo mais rápido em árvores profundas:**
DFS

**Algoritmo que usa mais memória:**
BFS

**Quando usar BFS:**
Quando queremos encontrar a solução **mais próxima da raiz**.

**Quando usar DFS:**
Quando queremos **explorar caminhos profundos ou todas as possibilidades**.

---


