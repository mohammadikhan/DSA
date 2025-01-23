# Implementation of Linear Search function

# Linear Search function to find the given target, which returns the index of the target
# and -1 if the target was not found
def linearSearch(arr, target):

    # Loop through all the elements in the array
    for i in range(len(arr)):
        
        # If the target is found, return its index in the array
        if arr[i] == target:
            return i
    
    return -1

if __name__=="__main__":

    # Create a list of numbers and specifiy a target and call the linear search function
    arr = [1, 11, 3, 5, 8, 9, 15, 17, 16]
    print("\nSearching for 15 in the array:", "Found " if linearSearch(arr, 15) != -1 else "Not found")
    print("\nSearching for 10 in the array:", "Found " if linearSearch(arr, 10) != -1 else "Not found")
