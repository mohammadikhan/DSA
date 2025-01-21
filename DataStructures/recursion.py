# Implementing recursive functions

# Recursive function to calculate the factorial of a number
def factorial(n):

    # Base Case: When n reaches 0, we return 1 since 0! = 1
    if n == 0:
        return 1
    
    # Recursive Case: Otherwise we multiply n by the recursive call on n - 1
    # Ex: If n == 5, then calling the recursive case would look like:
    # 5 * factorial(5 - 1) --> 5 * factorial(4)
    return n * factorial(n - 1)

# Recursive function to get the fibonacci sequence of a number
def fibonacci(n):
    
    # Base Case: If n is less than or equal to 1, return n
    if n <= 1:
        return n
    
    # Recursive Case: Return the sum of the recursive call on the (n - 1)th and (n - 2)th Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive Function to reverse a string
def reverseString(s):
    
    # Base Case: If the string is empty, return an empty string
    if len(s) == 0:
        return ""
    
    # Recursive Case: Return the recusrive call on the substring excluding the first character
    # and append the first character to the result
    return reverseString(s[1:]) + s[0]

if __name__=="__main__":

    # Testing Recursive functions  
    print("\nRecurisve Factorial function by calulcating factorial(5): ", factorial(5))
    print("\nRecursive Fibonacci function by calculating fibonacci(8): ", fibonacci(8))
    print("\nRecursive String reversal function by calling reverseString(hello): ", reverseString("hello"))

