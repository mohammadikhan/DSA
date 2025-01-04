
# Sets are mutable collection of data that does not allow for duplication
# Mainly used for membership testing and eliminating duplicate entries
# Data strucutre used in this is Hashing, a technique to perform insertion, deletion and traversal in O(1) on average

# Creating set with mixed values (Numbers and Strings)
Set = set([1,2,"Test", 4, "This", 5, "Out", 8])
print("\nSet with the use of Mixed Values")
print(Set)

# Acessing elements using for loop
print("\nElements of set: ")
for i in Set:
    print(i, end=" ")
print()

# Checking if element is in the set
print("Test" in Set) # --> True
print(30 in Set) # --> False


