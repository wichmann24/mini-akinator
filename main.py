from tree import create_tree
from search import dfs, bfs
from game import jogar

def main():
    root = create_tree()

    print("\nDFS:")
    dfs(root)

    print("\nBFS:")
    bfs(root)

    print("\nJogo de adivinhação")
    jogar(root)


if __name__ == "__main__":
    main()
