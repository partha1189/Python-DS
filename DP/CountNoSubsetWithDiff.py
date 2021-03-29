"""
Author: Partha Sen
"""
from CountSubsetSum import count_subset_sum

def count_subset_with_diff(arr, diff):
	s = (diff + sum(arr)) // 2
	#print(s)
	return count_subset_sum(arr, s, len(arr))
	
if __name__ == '__main__':
	print(count_subset_with_diff([1, 1, 2, 3], 1))
