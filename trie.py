import graphviz

words = ["enduro", "enduromtb", "endo", "moto"]

class Node:
    glob_id = 0
    def __init__(self):
        self.children = []
        self.character = ""
        self.finish = False
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id

    def __init__(self, char, finish):
        self.children = []
        self.character = char
        self.finish = finish
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id

    def findChar(self, char):
        for child in self.children:
            if child.character == char:
                return child
        return None

    def addNode(self, char, finish):
        newNode = Node(char, finish)
        self.children.append(newNode)
        return newNode

    def show(self):
        d = graphviz.Digraph("tree", filename='tree.gv')
        self.buildTree(d, self)
        d.view()

    def buildTree(self, d, node):
        label = "finish" if node.finish else ""
        d.node(str(node.id), node.character + label)
        for child in node.children:
            d.edge(str(node.id), str(child.id))
            self.buildTree(d, child)

root = Node("", False)

for word in words:
    lastNode = root
    wordLen = len(word)
    for i, character in enumerate(word):
        nodeWithChar = lastNode.findChar(character)
        if nodeWithChar is not None:
            lastNode = nodeWithChar
        else:
            lastNode = lastNode.addNode(character, wordLen - 1 == i)
root.show()
