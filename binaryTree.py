import graphviz

class Node:
    glob_id = 0
    def __init__(self, value):
        self.parent = None
        self.children = [None, None]
        self.value = value
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id

    def insert(self, node):
        if node.value > self.value:
            if self.children[1] is None:
                node.parent = self
                self.children[1] = node
            else:
                self.children[1].insert(node)
        else:
            if self.children[0] is None:
                node.parent = self
                self.children[0] = node
            else:
                self.children[0].insert(node)

    def hasChildren(self):
        return self.children[0] is not None and self.children[1] is not None

    def show(self):
        d = graphviz.Digraph("tree", filename='tree.gv')
        self.buildTree(d, self)
        d.view()

    def buildTree(self, d, node):
        d.node(str(node.id), str(node.value))
        for child in node.children:
            if child is not None:
                d.edge(str(node.id), str(child.id))
                self.buildTree(d, child)

root = Node(5)
root.insert(Node(2))
root.insert(Node(3))
root.insert(Node(7))
root.insert(Node(1))
root.insert(Node(8))
root.insert(Node(6))
root.show()