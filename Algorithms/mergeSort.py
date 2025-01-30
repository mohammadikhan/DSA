# Implementation of Merge Sort

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

if __name__=="__main__":
    
     # Create a list and call the merge sort algorithm
    arr = [43, 19, 25, 8, 9]
    print("\n------List before applying the Merge Sort Algorithm------")
    print("\t\t", arr)
    print("\n------List after applying the Merge Sort Algorithm------")
    print("\t\t", mergeSort(arr))
