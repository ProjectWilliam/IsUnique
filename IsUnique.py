#!/usr/bin/python
# Author: William Guerrero
# Checks if a string contains all unique characters


String = raw_input('Please enter a String to be checked: ');
	
def LetterCounter(x):
	
	uniquechars = set()
	
	for c in x:
	
		if c in uniquechars:
		
			print 'Input does not contain Unique Characters'
		
			return False
				
		uniquechars.add(c)
	
		print uniquechars
	
	print 'Input does contain Unique Characters'
	

	
#Calling function	
LetterCounter(String);
