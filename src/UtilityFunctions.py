from graphviz import Digraph
def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for parent in v.parents:
                edges.add((parent, v))
                build(parent)
    build(root)
    return nodes, edges

def draw_dot(root, format='svg', rankdir='LR'):
    """
    format: png | svg | ...
    rankdir: TB (top to bottom graph) | LR (left to right)
    """
    assert rankdir in ['LR', 'TB']
    nodes, edges = trace(root)
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir}) #, node_attr={'rankdir': 'TB'})

    for n in nodes:
        dot.node(name=str(id(n)), label = "{%s| data %.4f | grad %.4f}" % (n.label, n.data, n.grad), shape='record')
        if n.parents_operation:
            dot.node(name=str(id(n)) + n.parents_operation, label=n.parents_operation)
            dot.edge(str(id(n)) + n.parents_operation, str(id(n)))

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2.parents_operation)

    return dot