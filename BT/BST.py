class Node(object):
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class Tree(object):
    def __init__(self):
        self.root = None
    
    def add_Child(self,value):
        node = Node(value)
        if self.root== None:
            self.root = node
            return node
        else:
            currentNode = self.root
            added = False
            while not added and currentNode:
                if value == currentNode.value:
                    return "Duplicate found"
                
                if value < currentNode.value:
                    if currentNode.leftChild == None:
                        currentNode.leftChild = node
                        added= True
                        print("added left")
                    else:
                        currentNode = currentNode.leftChild
                elif value > currentNode.value:
                    if currentNode.rightChild == None:
                        currentNode.rightChild = node
                        added= True
                        print("added right")
                    else:
                        currentNode = currentNode.rightChild
    
    def in_order(self,node):
        if node==None:
            return
        self.in_order(node.leftChild)
        print(node.value)
        self.in_order(node.rightChild)



tree = Tree()
root_Node=tree.add_Child(4)
tree.add_Child(2)
tree.add_Child(5)
tree.add_Child(3)
tree.add_Child(11)
tree.add_Child(9)
tree.add_Child(10)
tree.add_Child(6)
tree.add_Child(12)
tree.in_order(root_Node)

