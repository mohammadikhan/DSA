# Dynamic Progamming Implementations of recursive functions

# Optimizing recursive fibonacci function using Memoization
def fibonacciM(n, memo):
    
    # Base Case: if n <= 1 we return n
    if n <= 1:
        return n

    # Check to see if the value already exists in the memo list
    if memo[n] != -1:
        return memo[n]
    
    # Caluclate and save the computed value to the memo list
    memo[n] = fibonacciM(n - 1, memo) + fibonacciM(n - 2, memo)

    return memo[n]

def fibonacci(n):
   
   # Initialize memo list with -1 (to inidicate that the value has not been calculated)
   memo = [-1] * (n + 1)
   return fibonacciM(n, memo)

# Optimizing recursive fibonacci function using Tabulation
def fibonacciT(n):
    
    # Create DP table to store fibonacci numbers
    dp = [0] * (n + 1)
    
    # Store independent values (0 and 1) in the the DP table
    dp[0] = 0
    dp[1] = 1

    # Fill the DP table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] 

if __name__=="__main__":
    
    print("\nCalling the optimized recursive fibonacci function using memoization: ", fibonacci(5))
    print("\nCalling the optimized recursive fibonacci function using tabulation: ", fibonacciT(10))
    