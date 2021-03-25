"""
Author: Partha Sen
"""
def min_subset_sum_difference(arr, n):
	sum = 0
	for i in range(n):
		sum += arr[i]
	t = subset_sum(arr, sum, n)
	mid = sum // 2
	for j in range(mid , -1, -1):
		if t[n][j] == True:
			#range - 2(s1)
			#here s1 = j
			return sum - (2 * j)
		
		
		
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
				
	return t
	
if __name__ == '__main__':
	print(min_subset_sum_difference([1, 2, 7], 3))
