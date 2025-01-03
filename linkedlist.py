class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def frontInsertion(self, newData):

        newNode = Node(newData)

        newNode.next = self.head

        self.head = newNode

    def insertAfter(self, prevNode, newData):

        if prevNode is None:
            print("\nNode must exist in the Linked List")
            return
        
        newNode = Node(newData)

        newNode.next = prevNode.next

        prevNode.next = newNode

    def insertBefore(self, key, newData):

        if self.head is None:
            return

        if self.head.data == key:
            newNode = Node(newData)
            newNode.next = self.head
            self.head = newNode
            return

        prev = None
        curr = self.head

        while curr is not None and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is not None:
            newNode = Node(newData)
            prev.next = newNode
            newNode.next = curr

    def endInsertion(self, newData):

        if self.head is None:
            self.head = Node(newData)

        newNode = Node(newData)

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode

    def frontDeletion(self):

        if self.head is None:
            print("Linked List is empty")
            return
        
        temp = self.head

        self.head = self.head.next

        del temp

    def endDeletion(self):

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            temp = self.head
            self.head = None
            del temp
            return

        secondLast = self.head
        while secondLast.next.next:
            secondLast = secondLast.next

        temp = secondLast.next
        secondLast.next = None
        del temp

    def deleteNode(self, node):

        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head == node:
            self.head = self.head.next
            del node
            return
        
        temp = self.head
        while temp.next and temp.next != node:
            temp = temp.next

        if temp.next is None:
            print("Node not found in the Linked List")
            return

        temp.next = node.next
        del node

    def search(self, key):

        curr = self.head
        
        while curr.next:

            if curr.data == key:
                return True
            curr = curr.next

        return False
    
    def recursiveSearch(self, node, key):

        if node is None:
            return False
        
        if node.data == key:
            return True
        
        return self.recursiveSearch(node.next, key)

    def listLength(self, head):
        if head is None:
            return 0

        return 1 + self.listLength(head.next) 
    

    def nthNode(self, size):
        length = 0
        temp = self.head

        while temp is not None:
            temp = temp.next
            length += 1

        if length < size:
            return -1
        
        temp = self.head

        print("Length: ", length)
        print("Size: ", size)

        for _ in range(1, length - size + 1):
            temp = temp.next

        return temp.data
    

    def reverseList(self):

        # Initialize pointers
        curr = self.head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        
        while prev:
            print(prev.data, end=" ")
            prev = prev.next

    def recursiveReverse(self, head):

        if head is None or head.next is None:
            return head

        rest = self.recursiveReverse(head.next)

        head.next.next = head

        head.next = None

        return rest   

    def reverse(self):
        self.head = self.recursiveReverse(self.head)  


def sortedMerge(head1, head2):
    
    arr = []

    # Adding the values of the first linked list
    while head1:
        arr.append(head1.data)
        head1 = head1.next

    # Adding the values of the second linked list:
    while head2:
        arr.append(head2.data)
        head2 = head2.next

    # Sort the list
    arr.sort()

    # Create New Linked List
    dummy = Node(0)
    curr = dummy

    for value in arr:
        curr.next = Node(value)
        curr = curr.next


    return dummy.next

def recursiveSortedMerge(head1, head2):

    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    if head1.data <= head2.data:
        head1.next = recursiveSortedMerge(head1.next, head2)
        return head1
    else:
        head2.next = recursiveSortedMerge(head1, head2.next)
        return head2
    

def printList(curr):

    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    

if __name__=="__main__":

    linkedList = LinkedList()
    linkedList.head = Node(1)
    second = Node(2)
    third = Node(3)

    linkedList.head.next = second
    second.next = third

    print("\nInitial Linked List: ")
    linkedList.printList()

    print("\nFront Insertion into Linked List: ")
    linkedList.frontInsertion(0)
    linkedList.printList()

    print("\nInserting after second node into Linked List: ")
    linkedList.insertAfter(second, 2.5)
    linkedList.printList()

    print("\nInserting at the end of the Linked List: ")
    linkedList.endInsertion(4)
    linkedList.printList()

    print("\nFront Deletion: ")
    linkedList.frontDeletion()
    linkedList.printList()

    print("\nEnd Deletion: ")
    linkedList.endDeletion()
    linkedList.printList()

    print("\nDelete Specific Node: ")
    linkedList.deleteNode(second)
    linkedList.printList()

    print("\nInserting before Node 2")
    linkedList.insertBefore(2.5, 5)
    linkedList.printList()

    # print("\nSearching for 5 in Linked List: ")
    # print(linkedList.search(5))

    # print("\nSearching for 6 in Linked List: ")
    # print(linkedList.search(6))
    
    # print("\nSearching for 6 in Linked List: ")
    # print(linkedList.recursiveSearch(linkedList.head, 6))

    # print("\nLength of the list: ")
    # print(linkedList.listLength(linkedList.head))

    print("\n1st node from the end of the linked list: ")
    print(linkedList.nthNode(2))

    # print("\nReversing the linked list: ")
    # linkedList.reverseList()

    # print("\nRecursively reversing the linked list: ")
    # linkedList.reverse()
    # linkedList.printList()
    
    linkedList2 = LinkedList()
    linkedList3 = LinkedList()

    linkedList2.head = Node(1)
    listSecond = Node(8)
    listThird = Node(16)

    linkedList2.head.next = listSecond
    listSecond.next = listThird

    linkedList3.head = Node(2)
    thirdSecond = Node(7)
    thirdThird = Node(14)

    linkedList3.head.next = thirdSecond
    thirdSecond.next = thirdThird

    print("\nSecond Linked List: ")
    linkedList2.printList()
    print("\nThird Linked List: ")
    linkedList3.printList()
    
    print("\nMerging the two Sorted Linked Lists")
    res = sortedMerge(linkedList2.head, linkedList3.head)
    printList(res)