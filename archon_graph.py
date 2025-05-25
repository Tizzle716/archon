import networkx as nx

class ArchonGraph:
    """
    Manages the project knowledge graph.
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, **attrs):
        """Add a node to the graph."""
        self.graph.add_node(node_id, **attrs)
