"""
Author: Partha Sen
"""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from Stack import Stack

def sort(s):
	if s.size() == 1:
		return 
	
	temp = s.pop()
	sort(s)
	insert(s, temp)
	return s

def insert(s, temp):
	if s.is_empty() or s.peek() <= temp:
		s.push(temp)
		return 
	val = s.pop()
	insert(s, temp)
	s.push(val)
	return s




s = Stack()
s.push(5)
s.push(1)
s.push(0)
s.push(2)

print(str(s))

print(str(sort(s)))
