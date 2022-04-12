
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

    def pre_order(self,node):
        if node==None:
            return
        print(node.value)
        self.pre_order(node.leftChild)
        self.pre_order(node.rightChild)

    def post_order(self,node):
        if node==None:
            return
        self.post_order(node.leftChild)
        self.post_order(node.rightChild)
        print(node.value)

    def level_order(self,node):
        my_queue =[]
        my_queue.append(node)
        ans=[]
        while my_queue:
            curr_list=[]
            curr_size=len(my_queue)
            while curr_size>0:
                node = my_queue.pop(0)
                curr_list.append(node.value)
                curr_size-=1
                print(node.value, end=' ')
                if node.leftChild != None:
                    my_queue.append(node.leftChild)
                if node.rightChild != None:
                    my_queue.append(node.rightChild)
            
            ans.append(curr_list)
        print(ans)

    def remove(self,value):
        current_node = self.root
        parent_node = None
        node_to_remove = None
        found = False
        while not found:
            if (current_node==None or current_node.value==None):
                print("node not found")
                return
            
            if (value==current_node.value):
                node_to_remove = current_node
                found = True
            elif value<current_node.value:
                parent_node= current_node
                current_node= current_node.leftChild
            else:
                parent_node = current_node
                current_node = current_node.rightChild

        
        node_to_remove_is_parent_left_child = parent_node.leftChild == node_to_remove

        if(node_to_remove.leftChild==None and node_to_remove.rightChild==None):
            if node_to_remove_is_parent_left_child:
                parent_node.leftChild=None
            else:
                parent_node.rightChild=None
        elif(node_to_remove.leftChild != None and  node_to_remove.rightChild == None):
            if node_to_remove_is_parent_left_child :
                parent_node.leftChild = node_to_remove.leftChild
            else:
                parent_node.rightChild = node_to_remove.leftChild
        elif(node_to_remove.rightChild != None and node_to_remove.leftChild == None):
            if node_to_remove_is_parent_left_child :
                parent_node.leftChild = node_to_remove.rightChild
            else:
                parent_node.rightChild = node_to_remove.rightChild
        else:
            right_tree = node_to_remove.rightChild
            left_tree = node_to_remove.leftChild
            if node_to_remove_is_parent_left_child:
                parent_node.leftChild = right_tree
            else:
                parent_node.rightChild = right_tree

            current_left_node=right_tree
            current_left_parent = None
            found_space_left = False

            while not found_space_left:
                if current_left_node == None:
                    found_space_left = True
                else:
                    current_left_parent = current_left_node
                    current_left_node = current_left_node.leftChild
            
            current_left_parent.leftChild=left_tree
            print("node sucessfully deleted")
            return


        



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
print("Before Remove")
#tree.in_order(root_Node)
#tree.remove(6)
#tree.remove(10)
#tree.remove(11)
print("After Remove Inorder")
#tree.in_order(root_Node)
print("After Remove PreOrder")
#tree.pre_order(root_Node)
#tree.post_order(root_Node)
tree.level_order(root_Node)