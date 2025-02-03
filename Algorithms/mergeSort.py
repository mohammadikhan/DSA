# Implementation of Merge Sort

# Merge function to merge two sorted sublists
def merge(arr, left, right, mid):
    
    # Calculate the lengths of the two sublists
    leftLen = mid - left + 1
    rightLen = right - mid

    # Create temporary lists to store left and right sublists
    L = [0] * leftLen
    R = [0] * rightLen

    # Copy the data from given list to the temporary left sublist
    for i in range(leftLen):
        L[i] = arr[left + i]
    
    # Copy the data from given list to the temporary right sublist
    for j in range(rightLen):
        R[j] = arr[mid + 1 + j]

    # Initialize indicies for the left, right and merged list
    i = j = 0
    k = left

    # Merge temporary lists back to the given list
    while i < leftLen and j < rightLen:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of the L temporary list to the given list
    while i < leftLen:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy remaining elements of the R temporary list to the given list
    while j < rightLen:
        arr[k] = R[j]
        j += 1
        k += 1

# Recurisve Merge Sort algorithm to to sort a list
def mergeSort(arr, left, right):
    
    # Base Case: if left index is less than right, the list consits of more than one element
    if left < right:
        # Calculate the mid to divide list into two halves
        mid = (left + right) // 2

        # Recursively call the function on the left half
        mergeSort(arr, left, mid)
        
        # Recursively call the function on the right half
        mergeSort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, right, mid)

if __name__=="__main__":
    
     # Create a list and call the merge sort algorithm
    arr = [43, 19, 25, 8, 9]
    print("\n------List before applying the Merge Sort Algorithm------")
    print("\t\t", arr)
    print("\n------List after applying the Merge Sort Algorithm------")
    mergeSort(arr, 0, len(arr) - 1)
    print("\t\t", arr)
