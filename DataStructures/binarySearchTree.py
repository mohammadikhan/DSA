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

    def insertion(self, root, value):
        pass

    def delete(self, root, value):
        pass


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