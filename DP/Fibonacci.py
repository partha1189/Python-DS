
#memoization (store sub problems)
#use dict, keys will be args to fn, value will be return value

def fib(n, memo={}):
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1
	memo[n] = fib(n-1, memo) + fib(n-2,memo)
	return memo[n]
	
	
val = fib(6)
val1 = fib(50)
print(val)
print(val1)
