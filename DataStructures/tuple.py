
# Tuples are similar to lists but they are immutable meaning that once they are created, it cannot be modified
# Like Lists, they can contain elements of various types
# Created by placing sequence of values seperated by commas with or without the use of parantheses for grouping of the data sequence

Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)

list1 = [1,2,3,4,5,6]
print("\nTuple using list: ")
Tuple = tuple(list1)

# Acessing elements using indexing
print("First element of tuple")
print(Tuple[0])

print("\nLast element of tuple")
print(Tuple[-1])