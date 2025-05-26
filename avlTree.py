import graphviz

class Node:
    glob_id = 0

    def __str__(self):
        return str(self.value)

    def __init__(self, value):
        self.parent = None
        self.children = [None, None]
        self.value = value
        self.height = 0
        self.balanceFactor = 0
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id

    def updateHeight(self):
        if self.children[0] is None and self.children[1] is None:
            self.height = 0
        else:
            self.height = max(self.getChildHigh(0), self.getChildHigh(1)) + 1
        self.updateBalanceFactor()
        if self.parent is not None:
            self.parent.updateBalanceFactor()

    def updateBalanceFactor(self):
        self.balanceFactor = self.getSubtreeHigh(1) - self.getSubtreeHigh(0)

    def getChildHigh(self, child):
        if self.children[child] is not None:
            return self.children[child].height
        else:
            return 0

    def getSubtreeHigh(self, child):
        height = self.getChildHigh(child)
        return height + 1 if self.children[child] is not None else 0


    def insert(self, node):
        parent = self.findParentNode(node)
        if node.value > parent.value:
            parent.children[1] = node
        else:
            parent.children[0] = node
        node.parent = parent

        return self.rebalance(node)

    def rebalance(self, node):
        parent = node.parent
        prevParent = node
        while parent is not None:
            parent.updateHeight()
            if parent.balanceFactor < -1:
                if prevParent.balanceFactor < 0:
                    #left left
                    prevParent = parent
                    parent = parent.rightRotate()
                elif prevParent.balanceFactor > 0:
                    # left right
                    toRotate = prevParent
                    prevParent = toRotate.leftRotate()
                    parent = parent.rightRotate()
                else:
                    raise Exception("left case bad condition")
            elif parent.balanceFactor > 1:
                if prevParent.balanceFactor > 0:
                    #right right
                    prevParent = parent
                    parent = parent.leftRotate()
                elif prevParent.balanceFactor < 0:
                    # right left
                    toRotate = prevParent
                    prevParent = toRotate.rightRotate()
                    parent = parent.leftRotate()
                else:
                    raise Exception("right case bad condition")
            else:
                prevParent = parent
                parent = parent.parent
        return prevParent

    def rightRotate(self):
        oldParent = self.parent
        self.parent = self.children[0]
        self.children[0].parent = oldParent
        rightChildOfRotatee = self.children[0].children[1]
        self.children[0].children[1] = self
        self.children[0] = rightChildOfRotatee
        if oldParent is not None:
            oldParent.children[1] = self.parent
        self.updateHeight()
        self.parent.updateHeight()
        if oldParent is not None:
            oldParent.updateHeight()
        return self.parent

    def leftRotate(self):
        oldParent = self.parent
        self.parent = self.children[1]
        self.children[1].parent = oldParent
        leftChildOfRotatee = self.children[1].children[0]
        self.children[1].children[0] = self
        self.children[1] = leftChildOfRotatee
        if oldParent is not None:
            oldParent.children[0] = self.parent
        self.updateHeight()
        self.parent.updateHeight()
        if oldParent is not None:
            oldParent.updateHeight()
        return self.parent

    def findParentNode(self, node):
        if node.value > self.value:
            if self.children[1] is None:
                return self
            else:
                return self.children[1].findParentNode(node)
        else:
            if self.children[0] is None:
                return self
            else:
                return self.children[0].findParentNode(node)

    def hasChildren(self):
        return self.children[0] is not None and self.children[1] is not None

    def inOrderPrecedessor(self):
        if self.parent is None:
            return None
        if self.children[0] is not None:
            return self.children[0].findMax()

        parent = self.parent
        current = self
        while parent is not None:
            if parent.children[1] == current:
                return parent
            else:
                parent = parent.parent
                current = parent
        return None


    def findMax(self):
        if self.children[1] is not None:
            return self.findMax(self.children[1])
        else:
            return self

    def show(self):
        d = graphviz.Digraph("tree", filename='tree.gv')
        self.buildTree(d, self)
        d.view()

    def buildTree(self, d, node):
        d.node(str(node.id), str(node.value) + ":" + str(node.height) + ":" + str(node.balanceFactor))
        for child in node.children:
            if child is not None:
                d.edge(str(node.id), str(child.id))
                self.buildTree(d, child)
#left right
#root = Node(50)
#root = root.insert(Node(40))
#root = root.insert(Node(55))
#root = root.insert(Node(30))
#root = root.insert(Node(45))
#root = root.insert(Node(44))
#root = root.insert(Node(35))
#root.show()

# right right
#root = Node(40)
#root = root.insert(Node(30))
#root = root.insert(Node(50))
#root = root.insert(Node(45))
#root = root.insert(Node(55))
#root.show()
#root = root.insert(Node(60))
#root = root.insert(Node(35))
#root.show()

# right left
root = Node(45)
root = root.insert(Node(40))
root = root.insert(Node(50))
root = root.insert(Node(48))
root = root.insert(Node(55))
root.show()
root = root.insert(Node(47))
root.show()
