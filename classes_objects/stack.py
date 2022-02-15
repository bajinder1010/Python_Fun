class Stack(object):
    def __init__(self):
        self.stack=[]
    def get_stack_elements(self):
        return self.stack.copy()
    def add_one(self,item):
        self.stack.append(item)
    def add_many(self,item,n):
        for i in range(n):
            self.stack.append(item)
    def remove_one(self):
        self.stack.pop()
    def remove_many(self,n):
        for i in range(n):
            self.stack.pop()
    def size(self):
        return len(self.stack)
    def peek(self):
        if self.is_empty():
            return "nothing to peek"
        else:
            return self.stack[len(self.stack)-1]
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print('|_',thing,'_|')
    def add_list(self,new_list):
        for elm in new_list:
            self.stack.append(elm)
    def is_empty(self):
        return len(self.stack)==0

pancakes = Stack()
pancakes.add_one("blueberry")
pancakes.add_many("choclate",1)
print(pancakes.size())
pancakes.remove_one()
print(pancakes.size())
pancakes.prettyprint()
pancakes.remove_one()
print(pancakes.peek())
print(pancakes.is_empty())
