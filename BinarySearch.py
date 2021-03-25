"""
Author: Partha Sen
"""
def binary_search(lst, left, right, key):
	
	while left <= right:
		mid = left + (right - left) // 2
		if lst[mid] == key:
			return mid
		
		if key > lst[mid]:
			left = mid + 1
		else:
			right = mid - 1
			
	return -1







if __name__ == '__main__':
	lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
	key = 111

	# Function call
	result = binary_search(lst, 0, len(lst) - 1, key)

	if result != -1:
		print("Element is present at index:", result)
	else:
		print("Element is not present in the list")
