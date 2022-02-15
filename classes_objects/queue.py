class queue(object):
    def __init__(self):
        self.queue=[]

    def insert_last(self,item):
        self.queue.append(item)
    
    def remove_first(self):
        self.queue.pop(0)

    def length_queue(self):
        return len(self.queue)

    def prettyprint(self):
        for thing in self.queue:
            print('|_',thing,'_|')


persons = queue()
persons.insert_last("bob")
persons.insert_last("bani")
persons.insert_last("preeti")
persons.prettyprint()
persons.remove_first()

print(persons.length_queue())
persons.prettyprint()
print(persons.length_queue())
persons.insert_last("aashi")
persons.prettyprint()

print(persons.length_queue())

persons.remove_first()
persons.prettyprint()
