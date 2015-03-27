""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import collections 

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	text_file = open(file_name,'r')
	text_string= text_file.read()
	#remove whitespace
	text_list = text_string.split()
	#take out the headers
	indicies = [i for i, x in enumerate(text_list) if x =="***"]
	text_list = text_list[indicies[1]:indicies[2]]
	#remove punctuation
	npunc_text_list=[]
	for element in text_list: 
		npunc_text_list.append(element.strip(string.punctuation))
	#lower case
	final_list=[]
	for element in npunc_text_list:
		final_list.append(element.lower())
	return final_list


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	counts = collections.Counter(word_list).most_common(n)
	basic_list=[]
	for word in counts:
		basic_list.append(word[0])
	return basic_list

if __name__ == '__main__':
	print get_top_n_words(get_word_list('sherlock.txt'),100)