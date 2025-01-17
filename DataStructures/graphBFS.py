# Implementation of Graph using Adjacency List (wil use this for BFS Traversal):
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


    # BFS (Breadth-First Search) implementation
    def breadthFirstSearch(self, source):

        # Initialize Queue with the source vertex
        # Create a list of the visted nodes (starting from the source vertex)
        queue = [source]
        visited = [source]

        while queue:
            # While the queue is not empty, pop from the queue, print the data
            vertex = queue.pop(0)
            print(vertex, end=" ")

            # Check the neighbouring vertices of the vertex we just printed
            # If they have not been visted, add them to the visited list and the queue
            # Process is repeated until the queue is empty
            for neighbour in self.adjList[vertex]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


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

    # Performning BFS on the graph (starting from vertex 2)
    print("\nPerforming BFS on the graph starting from vertex 2: ")
    graph.breadthFirstSearch(2)

    # Performning BFS on the graph (starting from vertex 0)
    print("\nPerforming BFS on the graph starting from vertex 0: ")
    graph.breadthFirstSearch(0)

    # Performning BFS on the graph (starting from vertex 1)
    print("\nPerforming BFS on the graph starting from vertex 1: ")
    graph.breadthFirstSearch(1)
