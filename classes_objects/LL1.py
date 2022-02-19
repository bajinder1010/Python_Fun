class singly_LL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def insert_first(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next=self.head
            self.head = node
    def insert_last(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail = node
    def display(self):
        node = self.head
        
        while(node!=None):
            print(node.value,end="->")
            node = node.next
        print("END")



class Node(object):
    def __init__(self,value):
        self.value =value
        self.next = None

ll=singly_LL()
ll.insert_first(2)
ll.insert_first(3)
ll.insert_first(4)
ll.insert_last(5)
ll.insert_first(6)
ll.display()


