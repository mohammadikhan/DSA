# Implementation of Insertion Sort

def insertionSort(arr):
    
    # Loop through the list starting from the second element
    # (We make the assumption that the first element is sorted)
    for i in range(1, len(arr)):

        # Store the current element that will be inserted into the sorted portion
        # Create an index variable j to be the index of the last element in the sorted portion
        key = arr[i]
        j = i - 1

        # Compare the key with the elements in the sorted portion of the list (right to left)
        # If an element is greater than they key, shift the element one position to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

if __name__=="__main__":
    
     # Create a list and call the insertion sort algorithm
    arr = [27, 12, 1, 14, 26]
    print("\n------List before applying the Insertion Sort Algorithm------")
    print("\t\t", arr)
    print("\n------List after applying the Insertion Sort Algorithm------")
    insertionSort(arr)
    print("\t\t", arr)
    