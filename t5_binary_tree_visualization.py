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


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_visualize(node, visited, color_step=16):
    if node is not None:
        visited.add(node.id)
        node.color = f"#{min(color_step * 2, 255):02X}96F0"
        color_step += 75
        dfs_visualize(node.left, visited, color_step)
        dfs_visualize(node.right, visited, color_step)


def bfs_visualize(tree_root):
    visited = set()
    queue = [tree_root]
    color_step = 16

    while queue:
        node = queue.pop(0)
        if node.id not in visited:
            visited.add(node.id)
            node.color = f"#{min(color_step * 2, 255):02X}96F0"
            color_step += 22

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def reset_colors(node):
    if node is not None:
        node.color = "skyblue"
        reset_colors(node.left)
        reset_colors(node.right)


def main():
    # Creating a tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Visualization
    dfs_visualize(root, set())
    draw_tree(root)

    # Restore colors for BFS
    reset_colors(root)

    bfs_visualize(root)
    draw_tree(root)


if __name__ == "__main__":
    main()
