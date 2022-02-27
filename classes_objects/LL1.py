class singly_LL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self,value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next=self.head
            self.head = node
        self.size+=1


    def insert_last(self,value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail = node
        self.size+=1

    def display(self):
        node = self.head
        while(node!=None):
            print(node.value,end="->")
            node = node.next
        print("END")

    def delete_first(self):
        if self.size == 0:
            return None
        elif self.size==1:
            self.head=None
            self.tail=None
            self.size-=1
        else:
            self.head= self.head.next
            self.size-=1

    def delete_last(self):
        if self.size == 0:
            return None
        elif self.size==1:
            self.head=None
            self.tail=None
            self.size-=1
        else:
            current = self.head
            while(current.next!=self.tail):
                current = current.next
            self.tail = current
            self.tail.next=None
            self.size-=1

    def get_node(self,index):
        iterator = 0
        if index > self.size-1 or index < 0:
            print("Not a valid index")
            return None
        else:
            node = self.head
            while(iterator<index):
                node = node.next
                iterator+=1
            return node

    
    def insert_at_index(self,value,index):
        if index==0:
            self.insert_first(value)
        elif index == self.size-1:
            self.insert_last(value)
        else:
            prev_node = self.get_node(index-1)
            prev_next = prev_node.next
            new_node = Node(value)
            prev_node.next=new_node
            new_node.next=prev_next
            self.size+=1
        
    
    def ll_length(self):
        print(self.size)




class Node(object):
    def __init__(self,value):
        self.value =value
        self.next = None

ll=singly_LL()

ll.insert_first(1)
ll.insert_first(2)
ll.insert_first(3)
ll.insert_first(4)
ll.insert_first(5)
ll.display()
ll.ll_length()
ll.delete_last()
ll.display()
ll.ll_length()
ll.delete_last()
ll.display()
ll.ll_length()
node = ll.get_node(1)
print('Value at index 1:',node.value)
ll.insert_at_index(9,0)
ll.display()
ll.insert_at_index(10,3)
ll.display()
node = ll.get_node(0)
print('Value at index 0:',node.value)
ll.insert_at_index(99,1)
ll.display()
ll.ll_length()



