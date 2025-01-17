# Implementation of Graph using Adjacency List:

class Graph:

    # Initialize dictionary to represent adjacency list and have the default graph be undirected
    def __init__(self, isDirected=False):
        self.adjList = {}
        self.isDirected = isDirected

    
    # Add a vertex to the graph (this will append an empty list to that vertex since initally the vertex has no neighbouring vertices)
    def addVertex(self, vertex):
        
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    # Add an edge to the graph
    def addEdge(self, u, v, weight=None):

        # Check to see if we are dealing with weighted edges and append accordingly
        if weight is None:
            self.adjList[u].append(v)
        else:
            self.adjList[u].append((v, weight))

        # Handle the case if the graph is undirected
        if not self.isDirected:
            if weight is None:
                self.adjList[v].append(u)
            else:
                self.adjList[v].append((u, weight))
        
    # Remove an edge from the graph
    def removeEdge(self, u, v):

        # Check to see if the vertex exists and if the destination vertex exists in the list
        # If it does, remove it from the list   
        if u in self.adjList and v in self.adjList[u]:
            self.adjList[u].remove(v)

        # Handle the case if the graph is undirected
        if v in self.adjList and u in self.adjList[v]:
            self.adjList[v].remove(u)

    # Check to see if a graph has an edge
    def hasEdge(self, u, v):
        
        # If the vertex exists, check its list to see if it has the destination vertex
        # if it does return true, otherwise the edge does not exist
        if u in self.adjList:
            return v in self.adjList[u]
        return False

    # Diplsaying the adjacency list in a clear and readable format
    def displayAdjList(self):
        
        print("\nAdjacency List: ")
        for vertex, neighbours in self.adjList.items():
            print(f"{vertex}: {neighbours}")

if __name__=="__main__":

    # Create a graph with 5 vertices
    graph = Graph()
    for i in range(5):
        graph.addVertex(i)

    # Create the edges and add them to the graph
    edges = [(0,1), (1,3), (3,4), (4,2), (0,2), (1,2), (1,4)]
    for u, v in edges:
        graph.addEdge(u, v)

    # Display the initial graph
    graph.displayAdjList()

    # Check to see if an edge exists in the graph
    print("\nIs the edge (1, 4) in the graph? ", "Yes" if graph.hasEdge(1, 4) else "No")
    print("Is the edge (2, 3) in the graph? ", "Yes" if graph.hasEdge(2, 3) else "No")

    # Remove an edge from the graph
    print("\nRemoving the edge (0, 2) from the graph...")
    graph.removeEdge(0, 2)
    print("\nUpdated Adjacency List: ")
    graph.displayAdjList()
