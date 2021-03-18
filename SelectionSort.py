"""
Author: Partha Sen
"""

def selection_sort(lst):
	
	for i in range(len(lst)):
		min_index = i
		for j in range(i+1, len(lst)):
			if lst[min_index] > lst[j]:
				min_index = j
	
		lst[i], lst[min_index] = lst[min_index], lst[i]
	
	
if __name__ == '__main__':
	
	lst = [4, 6, 3, 8, 1, 2]
	selection_sort(lst)
	
	print("Sorted lst: ", lst)
