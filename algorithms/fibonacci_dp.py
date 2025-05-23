def fibonacci_memoization(n, memo={}):
    """
    Calculate Fibonacci number using memoization.
    :param n: The position in the Fibonacci sequence.
    :param memo: Dictionary to store previously computed Fibonacci numbers.
    :return: Fibonacci number at position n.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_tabulation(n):
    """
    Calculate Fibonacci number using tabulation.
    :param n: The position in the Fibonacci sequence.
    :return: Fibonacci number at position n.
    """
    if n <= 2:
        return 1
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Simulation of fibonacci_memoization function

def simulate_fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}

    # Print the current state of memo
    print(f"Called with n = {n}, memo = {memo}")

    if n in memo:
        print(f"Returning memo[{n}] = {memo[n]}")
        return memo[n]

    if n <= 2:
        print(f"Base case reached for n = {n}, returning 1")
        return 1

    # Recursive calls
    print(f"Computing fibonacci_memoization({n - 1}) + fibonacci_memoization({n - 2})")
    memo[n] = simulate_fibonacci_memoization(n - 1, memo) + simulate_fibonacci_memoization(n - 2, memo)

    # Print the result of the computation
    print(f"Computed memo[{n}] = {memo[n]}")
    return memo[n]

# Example usage
if __name__ == "__main__":
    n = 10
    # print(f"Fibonacci number at position {n} using memoization: {fibonacci_memoization(n)}")
    # print(f"Fibonacci number at position {n} using tabulation: {fibonacci_tabulation(n)}")
    simulate_fibonacci_memoization(15)