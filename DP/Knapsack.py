"""
Author: Partha Sen
"""

#Knapsack Problem
# W[] ->weight array
# V[] ->value array
# W -> Weight Capacity
#Find max profit
#If problem has 1) Choice(can pick or neglect an item) 2)Optimize (max, min, largest, smallest etc) THEN ITS DP

def knapsack(W, V, weight_capacity, n):
	#base condition (if either n = 0 or weight_capacity = 0)
	dp = [[-1 for x in range(weight_capacity + 1)] for y in range(n + 1)]
	#print( dp[n])
	if n == 0 or weight_capacity == 0:
		return 0
	if dp[n][weight_capacity] != -1:
		return dp[n][weight_capacity]
		
	if W[n - 1] <= weight_capacity:
		dp[n][weight_capacity] = max((V[n - 1] + knapsack(W, V, weight_capacity - W[n - 1], n -1)), knapsack(W, V, weight_capacity, n - 1))
		return dp[n][weight_capacity]
	else:
		dp[n][weight_capacity] = knapsack(W, V, weight_capacity, n - 1)
		return dp[n][weight_capacity]
	
def knapsack_tabular(wt, val, W, n):
	dp = [[0 for x in range(W+1)] for y in range(n+1)]
	#t[n + 1][W + 1] = []
	#print(dp)
	for i in range(1, n+1):
		for j in range(1, W+1):
			if wt[i - 1] <= j:
				dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])
			else:
				dp[i][j] = dp[i-1][j] 
	return dp[n-1][W]
	
if __name__ == '__main__':
	#print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
	print(knapsack_tabular([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))

