def fibonacci (n, memo):
    #to call the function first time, pass an empty hash. it builds along the way
    if n==0 or n==1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

#Base cases are unaffected by memoization, but the recursive calls are optimized. The memo dictionary stores previously computed Fibonacci values, allowing for efficient retrieval and avoiding redundant calculations.
#before any recursion we first check if hash has any calculations already
#if so just return the stored value in memo
#if not compute per standard recursive definition and store the result in memo for future reference.