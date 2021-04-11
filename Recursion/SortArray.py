"""
Author: Partha Sen
"""

def sort(arr):
	if len(arr) == 1:
		return 
	temp = arr.pop()
	#print(temp)
	sort(arr)
	insert(arr, temp)
	return arr
	
def insert(arr, temp):
	if len(arr) == 0 or arr[-1] <= temp:
		arr.append(temp)
		return
	val = arr.pop()
	insert(arr, temp)
	arr.append(val)
	return arr
	
if __name__ == '__main__':
	print(sort([2, 3, 7, 6, 4, 5, 9]))
