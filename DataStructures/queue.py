# Queue (using List)

queue = []

# Adding to the Queue
queue.append('A')
queue.append('B')
queue.append('C')

print("Creating simple Queue...")
print(queue)

# Removing from the Queue
print("\nQueue after removing first two elements: ")
print(queue.pop(0))
print(queue.pop(0))
print(queue)


# Queue (using collections.deque)
from collections import deque
q = deque()

# Adding to the Queue
q.append('D')
q.append('E')
q.append('F')
print("\nCreating another simple Queue: ")
print(q)

# Removing from the Queue
print("\nQueue after removing first two elements: ")
print(q.popleft())
print(q.popleft())
print(q)