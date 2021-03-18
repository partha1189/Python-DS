"""
Author: Partha Sen
"""
def bubble_sort(lst):
	
	for i in range(len(lst)):
		
		for j in range(0, len(lst) - i - 1):
			
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				

if __name__ == '__main__':
	
	lst =[7, 3, 4, 8, 1, 5]
	
	bubble_sort(lst)
	print("Sorted list is :", lst)
