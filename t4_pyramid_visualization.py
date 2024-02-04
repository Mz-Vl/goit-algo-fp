import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:

        # Keep the node height
        node.height = layer
        graph.add_node(node.id, color=node.color,
                       label=str(node.val) + "\nheight: " + str(node.height))

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_heap_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_heap_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_heap_edges(tree, heap_root, pos)

    # Set the size of nodes in proportion to their height
    sizes = [float(data['label'].split('\n')[1].split(': ')[1]) * 500 for _, data in tree.nodes(data=True)]
    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=sizes, node_color=colors)
    plt.show()


def main():
    # Creating a binary heap
    heap_root = Node(10)
    heap_root.left = Node(8)
    heap_root.right = Node(5)
    heap_root.left.left = Node(6)
    heap_root.left.right = Node(3)
    heap_root.right.left = Node(2)

    # A binary heap representation
    draw_heap(heap_root)


if __name__ == "__main__":
    main()
