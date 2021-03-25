
def gridTraveler(m, n, memo={}):
	KEY = str(m) + "," + str(n)
	#print(KEY)
	if KEY in memo:
		return memo[KEY]
	if m == 1 and n == 1:
		return 1
	
	if m == 0 or n == 0:
		return 0
		
	memo[KEY] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
	return memo[KEY]
	
print(gridTraveler(2,3))
print(gridTraveler(18,18))
