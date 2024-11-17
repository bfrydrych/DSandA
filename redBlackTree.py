import graphviz

red = "red"
black = "black"

class Node:
    glob_id = 0
    def __init__(self, value, color=red):
        self.parent = None
        self.children = [None, None]
        self.value = value
        Node.glob_id = Node.glob_id + 1
        self.id = Node.glob_id
        self.color = color

    def leftRotate(self):
        selfParent = self.parent
        selfParentParent = selfParent.parent
        self.parent = selfParent.parent
        selfParent.parent = self
        selfPrevLeftChild = self.children[0]
        self.children[0] = selfParent
        selfParent.children[1] = selfPrevLeftChild
        selfParentParent.children[1] = self


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
        if node.value > parent.value:
            parent.children[1] = node
        else:
            parent.children[0] = node
        #node.repaint()

    def insertBalanced(self, node):
        parent = self.findParentNode(node)
        node.parent = parent
        node.color = red
        if node.value > parent.value:
            parent.children[1] = node
        else:
            parent.children[0] = node
        notPainted = self.repaint(node)
        if notPainted.color is red and notPainted.parent is red:
            



    def repaint(self, node):
        if node.parent.color is red and node.parent.parent is not None and node.parent.parent.children[1] is red:
            node.parent = black
            node.parent.parent = red
            node.parent.parent.children[1] = black
            return self.repaint(node.parent.parent)
        else:
            return node


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
        fontcolor = 'black'
        if node.color is black:
            fontcolor= 'white'

        d.node(str(node.id), str(node.value), fillcolor=node.color, style='filled', fontcolor=fontcolor)
        for child in node.children:
            if child is not None:
                d.edge(str(node.id), str(child.id))
                self.buildTree(d, child)

    def __str__(self):
        return str(self.value)

root = Node(11, black)
root.insert(Node(2, red))
root.insert(Node(1, black))
root.insert(Node(7, black))
root.insert(Node(5, red))
root.insert(Node(8, red))
root.insert(Node(14, black))
root.insert(Node(15, red))
root.show()

#root.findNode(18).leftRotate()
#root.show()
