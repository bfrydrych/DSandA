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
        if parent.children[0] is None:
            parent.children[0] = node
        else:
            parent.children[1] = node
        node.repaint()

    def repaint(self):
        if self.parent.color is red:
            self.parent.color = black
            self.parent.repaint()



    def findParentNode(self, node):
        if node.value > self.value:
            if self.children[1] is None:
                return self
            else:
                self.children[1].findParentNode(node)
        else:
            if self.children[0] is None:
                return self
            else:
                self.children[0].findParentNode(node)

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