""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah2.txt')
	2
	>>> update_counter('blah.txt')
	3
	"""
	if reset == True or exists('file_name') == False:
		#to initiate the counter and dump it in a new file
		counter = 1

		t1 = dump(counter,open('file_name','w'))
		
		
	elif reset == False and exists('file_name') == True:
		#to load, increment the counter, and put it back
		counter= load(open('file_name','r+'))

		counter +=1

		dump(counter, open('file_name','r+'))
	
	else: #incase God knows what happens 
		raise ValueError 

	return load(open('file_name','r+'))
if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))