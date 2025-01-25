# Implementation of Binary Search

# Iterative implemenation of Binary Search
def binarySearch(arr, target):
    
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

if __name__=="__main__":

    # Create sample sorted list and call the Binary Search function
    arr = [1, 3, 8, 16, 24, 32, 45]
    print("Searching for 8 in the list:", f"Found at index {binarySearch(arr, 8)}" if binarySearch(arr, 8) != -1 else "Not Found")
    print("Searching for 17 in the list:", f"Found at index {binarySearch(arr, 17)}" if binarySearch(arr, 17) != -1 else "Not Found")
    