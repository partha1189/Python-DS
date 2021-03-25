def howSum(targetSum, numbers, memo={}):
	if targetSum in memo:
		return memo[targetSum]
	if targetSum == 0:
		return list()
	
	if targetSum < 0:
		return None
		
	for n in numbers:
		REM = targetSum - n
		REM_RES = howSum(REM, numbers, memo)
		#print(REM_RES)
		if REM_RES is not None:
			REM_RES.append(n)
			memo[targetSum] = REM_RES
			return memo[targetSum]
	memo[targetSum] = None
	return None
	
print(howSum(7, [2, 3]))
print(howSum(8, [2, 3, 5]))
print(howSum(300,[7, 14]))
