
# Dictionary is an unordered collection of data that stores data in the format of key:value pair
# It is similar to hash tables in other languages with time complexity of O(1)
# Indexing is achieved using keys
# These are of any hashtable type, i.e an object whose can never change like strings, numbers, tuples, etc.
# It is created using curly braces or dictionary comprehension

# Creating a Dictionary
Dict = {'Name': 'Tester', 1: [1, 2, 3, 8]}
print("Creating Dictionary: ")
print(Dict)

# Accessing element using key
print("Accessing element using key: ")
print(Dict['Name'])

# Acessing element using get()
print("Accessing a element using get: ")
print(Dict.get('Name'))

# Creating dictionary using dictionary comprehension
print("\nCreating Dictionary using dictionary comprehension")
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)