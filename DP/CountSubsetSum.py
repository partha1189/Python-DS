"""
Author: Partha Sen
"""
def count_subset_sum(arr, sum, n):
	t = [[0 for x in range(sum+1)] for y in range(n+1)]
	for i in range(n+1):
		t[i][0] = 1
	#print(t)
	for i in range(1, n+1):
		#inner loop starting from zero(special case incase of sum zero)
		for j in range(0, sum+1):
			if arr[i - 1] <= j:
				t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
			else:
				t[i][j] = t[i-1][j]
	#print(t)
	return t[n][sum]
	
if __name__ == '__main__':
	print(count_subset_sum([2, 3, 5, 6, 8, 10], 10, 6))
	print(count_subset_sum([0, 0, 1, 0], 0, 4))
