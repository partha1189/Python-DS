"""
Author: Partha Sen
"""
import sys
def mcm(a, i, j):
	
	if i >= j:
		return 0
		
	_min = sys.maxsize
	
	for k in range(i, j-1):
		
		count = mcm(a, i, k) + mcm(a, k+1, j-1) + a[i-1] * a[k] * a[j-1]
		
		if count < _min:
			_min = count
		
	return _min
	
print(mcm([1, 2, 3, 4, 3], 1, 5))
