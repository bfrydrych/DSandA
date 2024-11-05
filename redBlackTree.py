import graphviz

red = "red"
black = "black"

class Node:
    glob_id = 0
    def __init__(self, value):
        self.parent = None
        self.children = [None, None]
        self.value = value
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id
        self.color = None

    def rightRotate(self):
        #pivot parent
        #child(self) becomes parent of it's parent
        #child's (self) parent becomes right child of self

        selfParent = self.parent
        selfParentParent = selfParent.parent
        selfParent.parent = self
        selfRightChildForLeftChildOfSelfNewChild = self.children[1]
        self.children[1] = selfParent

        #set former parent's parent as self's parent
        self.parent = selfParentParent

        # set self as child of former parent's parent
        for idx, child in enumerate(selfParentParent.children):
            if child == selfParent:
                selfParentParent.children[idx] = self
                break

        #after pivoting, change childs
        #left child of former parent becomes self's right child
        selfParent.children[0] = selfRightChildForLeftChildOfSelfNewChild

    def insert(self, node):
        parent = self.findParentNode(node)
        node.parent = parent
        node.color = red
        if node.value > parent.value:
            parent.children[1] = node
        else:
            parent.children[0] = node
        #node.repaint()

    def repaint(self):
        if self.parent.color is red:
            self.parent.color = black
            #self.parent.repaint()



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

    def findNode(self, value):
        if self.value == value:
            return self
        if value > self.value:
            if self.children[1] is not None:
                return self.children[1].findNode(value)
            else:
                return None
        else:
            if self.children[0] is not None:
                return self.children[0].findNode(value)
            else:
                return None

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

    def __str__(self):
        return str(self.value)

root = Node(7)
root.insert(Node(4))
root.insert(Node(3))
root.insert(Node(2))
root.insert(Node(6))
root.insert(Node(18))
root.insert(Node(11))
root.insert(Node(19))
root.insert(Node(14))
root.insert(Node(9))
root.insert(Node(12))
root.insert(Node(17))
root.insert(Node(22))
root.insert(Node(20))
#root.show()

root.findNode(11).rightRotate()
root.show()
