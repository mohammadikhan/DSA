# Implementation of Bubble Sort 

def bubbleSort(arr):
    
    # Store the length of the list
    n = len(arr) - 1

    # Loop through the entire list
    # After each pass. the largest element is placed in its correct position
    for i in range(n):

        # Create a flag to check if swaps are made in the current pass
        swapped = False

        # Loop through the unsorted porition of the list and compare adjacent elements
        # We reduce by 'i' after every pass as the last 'i' elements are already sorted
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap the two elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # Update the flag when a swap is made 
                swapped = True
        
        # If no swaps were made, the list is already sorted
        if not swapped:
            break


if __name__=="__main__":
    
    # Create a list and call the bubble sort algorithm
    arr = [17, 2, 1, 19, 43]
    print("\n------List before applying the Bubble Sort Algorithm------")
    print("\t\t", arr)
    print("\n------List after applying the Bubble Sort Algorithm------")
    bubbleSort(arr)
    print("\t\t", arr)
    