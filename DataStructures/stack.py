# Stack (Using List)

stack = []

stack.append('A')
stack.append('B')
stack.append('C')

print("\nPrinting the Stack: ")
print(stack)

# Calling pop() function in LIFO Order
print("\nPopping from the Stack: ")
print(stack.pop())
print(stack.pop())

print("\nStack after calling pop() twice: ")
print(stack)

# Calling append() (equivalent to push) function
print("\nPushing to the Stack...")
stack.append('D')
stack.append('E')


print("\nStack after pushing D and E: ")
print(stack)

# Stack (Using deque)
from collections import deque

stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')

print("\nPrinting the Stack: ")
print(stack)

# Calling pop() function in LIFO Order
print("\nPopping from the Stack: ")
print(stack.pop())
print(stack.pop())

print("\nStack after calling pop() twice: ")
print(stack)

# Calling append() (equivalent to push) function
print("\nPushing to the Stack...")
stack.append('D')
stack.append('E')


print("\nStack after pushing D and E: ")
print(stack)
