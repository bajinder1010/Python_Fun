
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

def Bfs(graph,start_value):
    start_node = graph.find_node(start_value)
    print(start_node.value)
    visited ={}
    for item in graph.nodes:
        visited[item.value]=False
    print(visited)
    queue =[]
    queue.append(start_node)
    while(queue):
        curr_node= queue.pop(0)
        if(visited[curr_node.value]==False):
            print(curr_node.value)
            visited[curr_node.value]=True
        for item in curr_node.edges:
            if(visited[item.value]==False):
                queue.append(item)


g= Graph(False)
g.add_node("5")
g.add_node("3")
g.add_node("7")
g.add_node("2")
g.add_node("4")
g.add_node("8")



g.add_edge("5","3")
g.add_edge("5","7")
g.add_edge("3","2")
g.add_edge("3","4")
g.add_edge("5","7")
g.add_edge("7","8")
g.add_edge("4","8")



print(len(g.nodes))
print(g.number_of_nodes())
g.number_of_edges()
#g.remove_node("preeti")
#print(len(g.nodes))
#print(g.number_of_nodes())
#g.number_of_edges()
print(g)
Bfs(g,"5")
