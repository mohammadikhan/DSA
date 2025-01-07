import heapq

# Create a list
l = [8, 6, 10, 12, 1]

# Create the heap by calling heapify
heapq.heapify(l)
print("Creating heap...")
print(l)

# Push 5 to the heap
heapq.heappush(l, 5)
print("Heap after pushing 5 to it: ")
print(l)

# Popping from the heap and printing the updated heap
print("Smallest element in the heap: ", end="")
print(heapq.heappop(l))

print("Heap after popping: ")
print(l)

