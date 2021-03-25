"""
Author: Partha Sen
"""

def subset_sum(arr, sum, n):
	t = [[False for x in range(sum + 1)] for y in range(n + 1)]
	for i in range(n+1):
		j = 0
		t[i][j] = True
	#print(t)
	for i in range(1, n+1):
		for j in range(1, sum+1):
			if arr[i-1] <= j:
				t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
			else:
				t[i][j] = t[i-1][j]
				
	return t[n][sum]
		
	
	
if __name__ == '__main__':
	print(subset_sum([2, 3, 7, 8, 10], 11, 5))
	print(subset_sum([3, 34, 4, 12, 5, 2], 9, 6))
