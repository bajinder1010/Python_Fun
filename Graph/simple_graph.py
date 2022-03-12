
class Node(object):
    def __init__(self,value):
        self.value = value
        self.edges = []

    def add_edge(self,node):
        self.edges.append(node)

    def __str__(self):
        returned_string = f"{self.value} -> "
        
        for edge in self.edges:
            returned_string += f"{edge.value} -> "  
     
        returned_string += "None"     
        return returned_string

class Graph(object):
    def __init__(self,undirected = False):
        self.undirected = undirected
        self.nodes =[]
    
    def add_node(self,value):
        self.nodes.append(Node(value))

    def remove_node(self,value):
        node_to_remove =self.find_node(value)
        self.nodes.remove(node_to_remove)
        for edge in node_to_remove.edges:
            if (edge.value==node_to_remove):
                node_to_remove.edges.remove(edge)
            

    def add_edge(self,value1,value2):
        node1 = self.find_node(value1)
        node2= self.find_node(value2)
        if(self.undirected==True):
           node1.add_edge(node2)
           node2.add_edge(node1)
        else:
            node1.add_edge(node2)
    
    def number_of_nodes(self):
        return f"The graph has {len(self.nodes)} nodes"

    def number_of_edges(self):
        for item in self.nodes:
            for edge in item.edges:
                print(edge.value)

    def find_node(self,value):
        for node in self.nodes:
            if node.value == value:
                return node
        print("no able to find node")
    
    def __str__(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph

g= Graph(False)
g.add_node("bob")
g.add_node("preeti")

g.add_edge("bob","preeti")

print(len(g.nodes))
print(g.number_of_nodes())
g.number_of_edges()
#g.remove_node("preeti")
#print(len(g.nodes))
#print(g.number_of_nodes())
#g.number_of_edges()

print(g)
