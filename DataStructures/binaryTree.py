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
    print("\nIn-Order Travesal: ", end="")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal: ", end="")
    first.preOrderTraversal(first)
    print("\nPost-Order Travesal: ", end="")
    first.postOrderTraversal(first)
