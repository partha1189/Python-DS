"""
Author: Partha Sen
"""

def print_LCS(x, y, m, n):
	t = length_of_LCS_tabular(x, y, m, n)
	print(t)
	i = m
	j = n
	res = ""
	while i>0 and j>0:
		if x[i-1] == y[j-1]:
			res += str(x[i-1])
			i -= 1
			j -= 1
		else:
			if t[i][j-1] > t[i-1][j]:
				j -=1
			else:
				i -=1
	print(res[::-1])
	return res[::-1]
	
	
def length_of_LCS_tabular(x, y, m, n):
	#Tabular(bottom-up) Solution
	t = [[0 for x in range(n+1)] for y in range(m+1)]
	
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i][j-1], t[i-1][j])
	return t
	
if __name__ == '__main__':
	print(print_LCS(['a', 'c', 'b', 'c', 'f'], ['a', 'b', 'c', 'd', 'a', 'f'], 5, 6))
