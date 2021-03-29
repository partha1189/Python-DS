"""
Author: Partha Sen
"""
#I/P  --->  X:  a b c d g h
#     --->  Y:  a b e d f h r
#O/P  --->  4 

def length_of_LCS(x, y, m, n):
	#Recursive Solution
	if m == 0 or n == 0:
		return 0
		
	if x[m-1] == y[n-1]:
		return 1 + length_of_LCS(x, y, m-1, n-1)
	else:
		return max(length_of_LCS(x, y, m, n-1), length_of_LCS(x, y, m-1, n))

def length_of_LCS_memoized(x, y, m, n):
	#Recursive + Memoized Solution
	t = [[-1 for x in range(n+1)] for y in range(m+1)]
	#print(t)
	return length_of_LCS_memoized_helper(x, y, m, n, t)
	
def length_of_LCS_memoized_helper(x, y, m, n, t):
	if t[m][n] != -1:
		return t[m][n]
	if m==0 or n==0:
		return 0
		
	if x[m-1] == y[n-1]:
		t[m][n] = 1 + length_of_LCS_memoized_helper(x, y, m-1, n-1, t)
		return t[m][n]
	else:
		t[m][n] = max(length_of_LCS_memoized_helper(x, y, m, n-1, t), length_of_LCS_memoized_helper(x, y, m-1, n, t))
		return t[m][n]
		
def length_of_LCS_tabular(x, y, m, n):
	#Tabular(bottom-up) Solution
	t = [[0 for x in range(n+1)] for y in range(m+1)]
	
	for i in range(1, m+1):
		for j in range(1, n+1):
			if x[i-1] == y[j-1]:
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i][j-1], t[i-1][j])
	return t[m][n]
		
print(length_of_LCS(['a', 'b', 'c', 'd', 'g', 'h'], ['a', 'b', 'e', 'd', 'f', 'h', 'r'], 6, 7))

print(length_of_LCS_memoized(['a', 'b', 'c', 'd', 'g', 'h'], ['a', 'b', 'e', 'd', 'f', 'h', 'r'], 6, 7))

print(length_of_LCS_tabular(['a', 'b', 'c', 'd', 'g', 'h'], ['a', 'b', 'e', 'd', 'f', 'h', 'r'], 6, 7))

#THIS IS FOR PALINDROME SEQUENCE
print(length_of_LCS_tabular(['a', 'g', 'b', 'c', 'b', 'a'], ['a', 'b', 'c', 'b', 'g', 'a'], 6, 6 ))
