"""
Author: Partha Sen
"""
from SubsetSum import subset_sum

def equal_sum_patition(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
		
	print(sum)
	if sum % 2 != 0:
		return False
	else:
		return subset_sum(arr, sum//2, len(arr))
	
	
if __name__ == '__main__':
	print(equal_sum_patition([1, 5, 11, 5]))
