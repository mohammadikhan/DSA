# Implemenation of Binary Search Tree and its operations

class Node:

    # Initalizing a node in a BST to have a data value, a left and right child
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Implementing In-Order Traversal
    def inOrderTraversal(self, root):
        
        if root is None:
            return
        
        self.inOrderTraversal(root.left)
        print(root.data, end=" ")
        self.inOrderTraversal(root.right)

    # Implementing Pre-Order Traversal
    def preOrderTraversal(self, root):
        
        if root is None:
            return

        print(root.data, end=" ")        
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    # Implementing Post-Order Traversal
    def postOrderTraversal(self, root):
        
        if root is None:
            return
        
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data, end=" ")

    # Implementing Lever-Order (BFS) Traversal
    def levelOrderTraversal(self, root):
        
        if root is None:
            return
        
        queue = [root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    # Searching for node in a BST
    def search(self, root, value):
        
        # If the tree is empty or value is found at the root, return the root
        if root is None or root.data == value:
            return root
        
        # If the value we are searching for is less than the value of the root,
        # recursively call the method on the left subtree
        if root.data > value:
            return self.search(root.left, value)
        
        # Otherwise the value is greater than the value of the root,
        # so recursively call the function on the right subtree
        return self.search(root.right, value)

    # Inserting a node in a BST
    def insertion(self, root, value):
        
        # Base case: Start from the root, and if we reach a leaf node with a value of NULL, create a node with the
        # the value we want to insert
        if root is None:
            return Node(value)
        
        # If the root's value is less than the value we are trying to insert.
        # go the right of the BST and recursively call the method on the right substree
        if root.data < value:
            root.right = self.insertion(root.right, value)
        # Otherwise, go to the left and recurse on the left subtree
        else:
            root.left = self.insertion(root.left, value)

        # Return the updated tree
        return root

    # Deleting a node from a BST
    def delete(self, root, value):
        
        # Base Case: If the tree is empty or if we reach a node that is NULL, return it
        if root is None:
            return root
        
        # Recursively call the delete function on the left subtree if the value we are deleting
        # is less than the root value
        if root.data > value:
            root.left = self.delete(root.left, value)

        # Else if the value is greater than the root value, recursively call the delete function on the
        # right subtree 
        elif root.data < value:
            root.right = self.delete(root.right, value)

        # Once we have found the node to delete we need to handle the three cases:
        # 1. If the node to delete is a leaf node
        # 2. If the node to delete has a single child
        # 3. If the node has two children
        else:

            # Handle cases if node to delete is a leaf node or has a single child
            # If there is no left child, return the right child
            if root.left is None:
                return root.right
            
            # If there is no right child, return the left child
            if root.right is None:
                return root.left
            
            # Hanlde case where node to delete has two children
            # Find the in-order successor (smallest value in the right subtree)
            successor = self.retrieveSuccessor(root)

            # Replace the current node's value with the successor's value
            root.data = successor.data

            # Delet the inorder successor from the right subtree
            root.right = self.delete(root.right, successor.data)
        
        return root
    
    # Helper method to get the inorder successor (smallest node in the right subtree)
    def retrieveSuccessor(self, current):
        
        # Go to the right subtree as this is where the smallest node will be located
        current = current.right

        # Keep traversing to the left until we find the smallest node and return it
        while current is not None and current.left is not None:
            current = current.left
        
        return current


if __name__=="__main__":

    # Creating nodes for BST
    first = Node(50)
    second = Node(30)
    third = Node(70)
    fourth = Node(20)
    fifth = Node(40)
    sixth = Node(60)
    seventh = Node(80)

    # Forming BST by connecting the nodes
    first.left = second
    first.right = third
    second .left = fourth
    second.right = fifth
    third.left = sixth
    third.right = seventh

    # Performing traversal methods on BST
    print("\nIn-Order Traversal: ", end=" ")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal: ", end=" ")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal: ", end=" ")
    first.postOrderTraversal(first)
    print("\nLevel-Order Traversal: ", end=" ")
    first.levelOrderTraversal(first)

    # Searching for 60 in the BST
    print("\n\nSearching for 60 in the BST... ")
    if first.search(first, 60):
        print("Value was found in the BST")
    else:
        print("Value does not exist in the BST")

    # Searching for 100 in the BST
    print("\n\nSearching for 100 in the BST... ")
    if first.search(first, 100):
        print("Value was found in the BST")
    else:
        print("Value does not exist in the BST")

    # Inserting 65 into the BST and perform traversal again
    print("\nInserting 65 in the BST... ")
    first.insertion(first, 65)
    print("\nIn-Order Traversal after insertion: ", end=" ")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal after insertion: ", end=" ")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal after insertion: ", end=" ")
    first.postOrderTraversal(first)
    print("\nLevel-Order Traversal after insertion: ", end=" ")
    first.levelOrderTraversal(first)

    # Deleting 50 from the BST and perform traversal again
    print("\n\nDeleting 50 in the BST... ")
    first.delete(first, 50)
    print("\nIn-Order Traversal after deletion: ", end=" ")
    first.inOrderTraversal(first)
    print("\nPre-Order Traversal after deletion: ", end=" ")
    first.preOrderTraversal(first)
    print("\nPost-Order Traversal after deletion: ", end=" ")
    first.postOrderTraversal(first)
    print("\nLevel-Order Traversal after deletion: ", end=" ")
    first.levelOrderTraversal(first)
