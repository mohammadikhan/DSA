# Implementation of Graph using Adjacency Matrix

class Graph:

    # Initialze the number of vertices, if the graph is directed or not (default is undirected)
    # and the adjacency matrix (which is V x V where V is the number of vertices)
    def __init__(self, numVertices, isDirected=False):
        self.numVertices = numVertices
        self.isDirected = isDirected
        self.adjMatrix = [[0 for _ in range(numVertices)] for _ in range(numVertices)]

    # Adding an edge to the graph (default weight of edges is 1)
    def addEdge(self, u, v, weight=1):

        self.adjMatrix[u][v] = weight

        # If the graph is undirected we need to make sure that an edge between u and v
        # means that there is an edge between v and u
        if not self.isDirected:
            self.adjMatrix[v][u] = weight

    
    # Removing an edge from the graph
    def removeEdge(self, u, v):

        self.adjMatrix[u][v] = 0

        # If the graph is undirected we need to make sure that removing an edge between u and v
        # means that we remove an edge between v and u
        if not self.isDirected:
            self.adjMatrix[v][u] = 0

    # Checking if the graph has an edge (if weight for edge is 0, there is no edge)
    def hasEdge(self, u, v):
        return self.adjMatrix[u][v] != 0
    
    
    # Display the graph in a readable format
    def printAdjMatrix(self):

        print("\nAdjacency Matrix of the Graph: ")
        for row in self.adjMatrix:
            print(row)


if __name__=="__main__":
    
    # Create an undirected Graph with 5 vertices
    graph = Graph(5)

    # Create a list of edges and add them to the graph
    edges = [(0,1), (1,3), (3,4), (4,2), (0,2), (1,2), (1,4)]
    for u, v in edges:
        graph.addEdge(u, v)

    # Display the graph
    graph.printAdjMatrix()

    # Check to see if an edge exists in the graph
    print("\nDoes the graph have edge (0, 1)? ", "Yes" if graph.hasEdge(0, 1) else "No")
    print("Does the graph have edge (0, 3)? ", "Yes" if graph.hasEdge(0, 3) else "No")

    # Remove an edge from the graph and display the updated graph
    print("Removing edge (1, 4)...")
    graph.removeEdge(1, 4)
    graph.printAdjMatrix()
    