import graphviz

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

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

    def insert(self, word):
        lastNode = self
        wordLen = len(word)
        for i, character in enumerate(word):
            nodeWithChar = lastNode.findChar(character)
            if nodeWithChar is not None:
                lastNode = nodeWithChar
            else:
                lastNode = lastNode.addNode(character, wordLen - 1 == i)

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

def findRootWord(node, word):
    lastNode = node
    rootWord = ""
    for char in word:
        node = lastNode.findChar(char)
        if node is not None and not node.finish:
            rootWord = rootWord + node.character
            lastNode = node
        if node is not None and node.finish:
            return rootWord + node.character
        if node is None:
            return None

root = Node("", False)

for word in dictionary:
    root.insert(word)

rootWords = []
newSentence = []
words = sentence.split()
for word in words:
    rootWord = findRootWord(root, word)
    if rootWord:
        newSentence.append(rootWord)
    else:
        newSentence.append(word)

print(newSentence)
