# Implementation of Selection Sort

def selectionSort(arr):

    # Traverse the unsorted portion of the list
    for i in range(len(arr)):

        # Initially we say that the current index holds the minimum element
        min = i

        # Traverse the remaining unsorted position to find the minimum element
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                # Once the minimum element is found, point the minimum index to the index of the minimum element
                min = j

        # Swap the smallest element with the elemnet of the current index
        arr[i], arr[min] = arr[min], arr[i]
    

if __name__=="__main__":
    
    # Create a list and call the selection sort algorithm
    arr = [12, 5, 4, 27, 8]
    print("\n------List before applying the Selection Sort Algorithm------")
    print("\t\t", arr)
    print("\n------List after applying the Selection Sort Algorithm------")
    selectionSort(arr)
    print("\t\t", arr)
