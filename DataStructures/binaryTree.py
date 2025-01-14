# Implementation of Binary Tree
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inOrderTraversal(self, node):

        if node is None:
            return
        
        self.inOrderTraversal(node.left)
        print(node.data, end=" ")
        self.inOrderTraversal(node.right)

    def preOrderTraversal(self, node):
        
        if node is None:
            return
        
        print(node.data, end=" ")
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):

        if node is None:
            return
        
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.data, end=" ")

    def levelOrderTraversal(self, root):

        if root is None:
            return
        
        # Create a queue, which initially contains the root node (since we are going by level)
        queue = [root]
        while queue:
            # Store the first element of the queue in a variable which holds the node and print its value
            node = queue.pop(0)
            print(node.data, end=" ")
            # If the node has a left child, add it to the queue and repeat the process
            if node.left:
                queue.append(node.left)
            # If the node has a right child, add it to the queue and repeat the prcoess
            if node.right:
                queue.append(node.right)

    # Inserting in a new node to a Binary Tree
    def insertion(self, root, value):

        # If the tree is empty, create the new node as the root
        if root is None:
            root = Node(value)
            return
        
        # Otherwise, do a level-order traversal until we find a place in the tree where a node points to NULL
        # Done using a queue, with the root initially in the queue
        queue = [root]
        while queue:

            # Store the node in a variable which will be used for the checking of null values
            temp = queue.pop(0)

            # If a nodes left child is not null, add the node to the queue
            # Otherwise insert the new node at that position and return the root
            if temp.left:
                queue.append(temp.left)
            else:
                temp.left = Node(value)
                return root        
            
            # If a nodes right child is not null, add the node to the queue
            # Otherwise insert the new node at that position and return the root
            if temp.right:
                queue.append(temp.right)
            else:
                temp.right = Node(value)
                return root
    
    # Search for a node in a binary tree (DFS Implementation)
    def search(self, root, value):

        # Handle base case if the node is null (or tree is empty) return false
        if root is None:
            return False
        
        # If the nodes value is equal to the value we are searching for, return true
        if root.data == value:
            return True
        
        # Recursively call the function on the left and right subtrees
        left = self.search(root.left, value)
        right = self.search(root.right, value)

        return left or right
    
    def delete(self, root, value):

        # If tree is empty, return NULL
        if root is None:
            return None
        
        # Perform BFS to find the node we want to remove
        queue = [root]
        targetNode = None

        while queue:
            node = queue.pop(0)

            # If we find the node we want to remove, store it in a variable to be used later to update its value
            if node.data == value:
                targetNode = node
                break

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
        # If we don't find the node we want to delete, return the tree as it is
        if targetNode is None:
            return root
        
        # Find the rightmost and deepest node in the tree
        # Create variables to hold the last node and its parent, initially set to NULL
        # Perform BFS to find the deepest and rightmost node
        lastNode, lastParent = None, None
        queue = [(root, None)]

        while queue:
            currentNode, parent = queue.pop(0)
            lastNode = currentNode
            lastParent = parent

            if currentNode.left:
                queue.append((currentNode.left, currentNode))

            if currentNode.right:
                queue.append((currentNode.right, currentNode))
        
        # Replace the target nodes data (the node we want to remove) with the data of the last node 
        targetNode.data = lastNode.data

        # Remove the deepest node by setting the reference to it as NULL
        if lastParent:
            if lastParent.left == lastNode:
                lastParent.left = None
            else:
                lastParent.right = None
        else:
            return None
        
        # Return the updated tree
        return root

if __name__=="__main__":

    # Create four nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Connect the nodes to form binary tree
    first.left = second
    first.right = third
    second.left = fourth

    # Call In-Order, Pre-Order and Post-Order traversal on the binaray tree constructred above
    print("\nDepth First Search Traversal Methods: ")
    print("\nIn-Order Traversal: ", end="")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal: ", end="")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal: ", end="")
    first.postOrderTraversal(first)

    print()
    print("\nBreadth First Search Traversal: ")
    print("\nLevel-Order Traversal: ", end="")
    first.levelOrderTraversal(first)

    # Performing Insertion on the binary tree by adding the value 5
    first.insertion(first, 5)
    print("\n\nAfter Insertion: ")
    print("\nIn-Order Traversal after insertion: ", end="")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal after insertion: ", end="")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal after insertion: ", end="")
    first.postOrderTraversal(first)
    print("\nLevel-Order Traversal after insertion: ", end="")
    first.levelOrderTraversal(first)

    # Searching for 2 and 6 in the binary tree
    print("\n\nSearching for 2 in the Binary Tree: ", first.search(first, 2))
    print("Searching for 6 in the Binary Tree: ", first.search(first, 6))

     # Performing Deletion on the binary tree by deleting the value 3
    print("\nDeleteing 3 from the Binary Tree... ")
    first.delete(first, 3)
    print("\nAfter Deletion: ")
    print("\nIn-Order Traversal after deletion: ", end="")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal after deletion: ", end="")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal after deletion: ", end="")
    first.postOrderTraversal(first)
    print("\nLevel-Order Traversal after deletion: ", end="")
    first.levelOrderTraversal(first)
