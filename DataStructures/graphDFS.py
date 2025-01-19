# Implementation of Graph using Adjacency List (wil use this for DFS Traversal):
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


    # DFS (Depth-First Search) recusrive implementation
    def depthFirstSearchRecusrive(self, source, visited=None):
        
        # If visited set is not provided, we create a visited set
        if visited is None:
            visited = set()
        
        # If the source (or starting vertex) has not been visited, add it to the set and print the vertex
        # Check the adjacet neighbours of this vertex and resursively call the function on the neighbouring vertices
        if source not in visited:
            visited.add(source)
            print(source, end=" ")
            for neighbour in self.adjList[source]:
                self.depthFirstSearchRecusrive(neighbour, visited)

    # DFS (Depth-First Search) iterative implementation
    def depthFirstSearchIterative(self, source):
        
        # Create a stack (for backtracking, initially we have the source vertex in the stack) and set for the visited vertices
        stack = [source]
        visited = set()

        # While the stack is not empty, pop from the stack add it to the set (if it is not already in the stack) and print the vertex
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")
            
            # Check the neighbouring vertices for the vertex we just popped and if they have not been visited, add them to the stack
            for neighbour in self.adjList[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)

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

    # Performing Recursive DFS on the graph (starting from vertex 2)
    print("\nPerforming Recursive DFS on the graph starting from vertex 2: ")
    graph.depthFirstSearchRecusrive(2)

    # Performing Recursive DFS on the graph (starting from vertex 0)
    print("\nPerforming Recursive DFS on the graph starting from vertex 0: ")
    graph.depthFirstSearchRecusrive(0)

    # Perforning Recursive DFS on the graph (starting from vertex 1)
    print("\nPerforming Recursive DFS on the graph starting from vertex 1: ")
    graph.depthFirstSearchRecusrive(1)

    print("\n\n------------------------------------------------------------")
    # Performing Iterative DFS on the graph (starting from vertex 2)
    print("\nPerforming Iterative DFS on the graph starting from vertex 2: ")
    graph.depthFirstSearchIterative(2)

    # Performing Recursive DFS on the graph (starting from vertex 0)
    print("\nPerforming Iterative DFS on the graph starting from vertex 0: ")
    graph.depthFirstSearchIterative(0)

    # Perforning Recursive DFS on the graph (starting from vertex 1)
    print("\nPerforming Iterative DFS on the graph starting from vertex 1: ")
    graph.depthFirstSearchIterative(1)
    