# Implementation of Binary Search

# Iterative implemenation of Binary Search
def binarySearchI(arr, target):
    
    # Determine the first and last indices of the list
    low = 0
    high = len(arr) - 1

    # Continue search while the search interval is valid
    while low <= high:
        
        # Calculate the middle index
        mid = (low + high) // 2

        # If the middle element is equal to the target, return the middle index
        if arr[mid] == target:
            return mid
        
        # If the middle element is greater than the target, search the left half
        elif arr[mid] > target:
            high = mid - 1

        # If the middle element is less than the target, search the right half
        else:
            low = mid + 1
    
    return -1

# Recursive implemenation of Binary Search
def binarySearchR(arr, low, high, target):

    # Check if the current search space is valid
    if high >= low:

        # Calculate the middle index of the current search range
        mid = (low + high) // 2
        
        # Base Case: If the middle element is the target, return the middle index
        if arr[mid] == target:
            return mid
        
        # If the middle element is greater than the target, recursively call the function on the left half
        elif arr[mid] > target:
            return binarySearchR(arr, low, mid - 1, target)
        # If the middle element is less than the target, recursively call the function on the right half
        else:
            return binarySearchR(arr, mid + 1, high, target)
    
    # Otherwise, the element was not found
    else:
        return -1

if __name__=="__main__":

    # Create sample sorted list and call the Binary Search function
    arr = [1, 3, 8, 16, 24, 32, 45]
    print("\n------------Iterative Binary Search------------")
    print("Searching for 8 in the list:", f"Found at index {binarySearchI(arr, 8)}" if binarySearchI(arr, 8) != -1 else "Not Found")
    print("Searching for 17 in the list:", f"Found at index {binarySearchI(arr, 17)}" if binarySearchI(arr, 17) != -1 else "Not Found")
    
    print("\n------------Recursie Binary Search------------")
    print("Searching for 32 in the list:", f"Found at index {binarySearchR(arr, 0, len(arr) - 1, 32)}" if binarySearchR(arr, 0, len(arr) - 1, 32) != -1 else "Not Found")
    print("Searching for 4 in the list:", f"Found at index {binarySearchR(arr, 0, len(arr) - 1, 4)}" if binarySearchR(arr, 0, len(arr) - 1, 4) != -1 else "Not Found")