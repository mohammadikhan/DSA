import heapq

# Min-Heap
# Create a list
l = [8, 6, 10, 12, 1]

# Create the min-heap by calling heapify
heapq.heapify(l)
print("Creating the min-heap...")
print(l)

# Push 5 to the min-heap
heapq.heappush(l, 5)
print("Min-heap after pushing 5 to it: ", end="")
print(l)

# Popping from the heap and printing the updated heap
print("Smallest element in the heap: ", end="")
print(heapq.heappop(l))

print("Min-heap after popping: ", end="")
print(l)

# Max-Heap
# Create another list and multiply values by negative one
maxL = [2, 17, 11, 16, 5]
maxL = [i * -1 for i in maxL]

# Creating max heap
heapq.heapify(maxL)
print("Creating max-heap...")
print([i * -1 for i in maxL])

# Pushing 12 to the heap
heapq.heappush(maxL, -12)
print("Heap after pushing 12 to it: ", end="")
print([i * -1 for i in maxL])

# Popping root from the max-heap and printing the updated heap
print("Largest element in the heap: ", end="")
print(heapq.heappop(maxL) * -1)
print("Max-heap after popping: ", end="")
print([i * -1 for i in maxL])
