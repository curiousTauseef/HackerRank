from queue import Queue
import copy
import random


def max_even_forest(graph):
    """
    Takes as input a tree, and returns the maximum number of edges which can be removed from the graph such that the
    resulting forest has trees which only have an even number of nodes in them.
    :param graph: a tree in the form of a dictionary mapping nodes to a set of their neighbors
    :return: an integer which the maximum number of edges which can be removed from the graph
    """

    stack = []
    parents = {}
    nodes = list(graph.keys())

    # Get a random node to be the "root" of this undirected graph
    root = nodes[random.randint(0, len(nodes))]

    # Modified BFS from the root node
    q = Queue()
    q.put(root)
    stack.append(root)
    while not q.empty():
        node = q.get()
        for nbr in graph[node]:
            if nbr not in stack:
                q.put(nbr)
                parents[nbr] = node
                stack.append(nbr)

    # Now from the parents mapping and our stack, make a mapping from each non-root node to the number of its "children"
    subtree_size = {}
    while len(stack) > 1:
        node = stack.pop()
        subtree_size[node] = 1
        neighbors = copy.copy(graph[node])

        # Remove the parent of the node from its neighbors to only consider "children"
        neighbors.remove(parents[node])

        for nbr in neighbors:
            subtree_size[node] += subtree_size[nbr]

    # Simply scan the resulting mapping, and return the value of the number of "even" subtrees found - 1
    count = 0
    for node in subtree_size:
        if subtree_size[node] % 2 == 0:
            count += 1

    return count


def run():
    """
    "Main" method. Usage:
        First line of input is the number of vertices (N) and the number of edges (M)
        The next M lines contain the edges as specified by the connected nodes

        Prints the integer number to the problem described here: https://www.hackerrank.com/challenges/even-tree
    :return: None, prints result
    """

    # Set up the graph
    line = input()
    num_vertices = int(line.split()[0])
    num_edges = int(line.split()[1])

    graph = {}
    for idx in range(1, num_vertices + 1):
        graph[idx] = []

    for dummy in range(num_edges):
        line = input()
        node1 = int(line.split()[0])
        node2 = int(line.split()[1])

        graph[node1].append(node2)
        graph[node2].append(node1)

    print(max_even_forest(graph))


run()
