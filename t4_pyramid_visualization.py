import heapq
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


def build_heap_tree(heap_list):
    heap_tree_root = Node(heap_list[0])
    for value in heap_list[1:]:
        add_to_heap_tree(heap_tree_root, value)
    return heap_tree_root


def add_to_heap_tree(node, value):
    if not node.left:
        node.left = Node(value)
    elif not node.right:
        node.right = Node(value)
    else:
        if value < node.left.val:
            add_to_heap_tree(node.left, value)
        else:
            add_to_heap_tree(node.right, value)


def add_heap_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:

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
    heap_lst = [1, 3, 5, 7, 9, 2, 4, 34]
    heapq.heapify(heap_lst)

    heap_tree_root = build_heap_tree(heap_lst)

    draw_heap(heap_tree_root)


if __name__ == "__main__":
    main()
