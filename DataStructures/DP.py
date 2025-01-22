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

# Function to determine the maximum profit for the Rod Cutting Problem using memoization
def rodCuttingMaxProfit(i, price, memo):

    # Handle the base case (length of 0 means no profit)
    if i == 0:
        return 0
    
    # Check if the value exists in the memo table
    if memo[i - 1] != -1:
        return memo[i - 1]
    
    maxProfit = 0

    # For each cut of length j, determine the maximum value by considering
    # the value for the current cut and recursively find the value of the remaining
    # rod of length (i - j)
    for j in range(1, i + 1):
        maxProfit = max(maxProfit, price[j - 1] + rodCuttingMaxProfit(i - j, price, memo))

    memo[i - 1] = maxProfit

    return maxProfit

# Function to initialize the memo tabel and to call the memoization function with rod length n
def rodCut(price):

    n = len(price)
    memo = [-1] * n
    return rodCuttingMaxProfit(n, price, memo)

# Function to determine the maximum profit for the Rod Cutting Problem using tabulation
def rodCutT(price, n):

    # Create a DP table to store the max profit for each length, where n is the length of the of the rod
    dp = [0] * (n + 1)

    # Build the table DP iteratively
    for i in range(1, n + 1):
        maxProfit = 0
        for j in range(1, i + 1):
            maxProfit = max(maxProfit, price[j - 1] + dp[i - j])
        dp[i] = maxProfit

    return dp[n]
    
if __name__=="__main__":
    
    print("\nCalling the optimized recursive fibonacci function using memoization: ", fibonacci(5))
    print("\nCalling the optimized recursive fibonacci function using tabulation: ", fibonacciT(10))

    print("\nCalling the optimized function to solve the rod cutting problem using memoization: ")

    price = [1, 5, 8, 9]
    print("The maximum profit of cutting up the rod is: $", rodCut(price))

    print("\nCalling the optimized function to solve the rod cutting problem using tabulation: ")
    print("The maximum profit of cutting up the rod is: $", rodCutT(price, len(price)))
