#Simple program that searches through text files and identifies phone numbers.

import sys
import re

def isPhoneNumber(text):
	#regex for phone numbers
	phone_regexes = re.compile(r'\d{3}-\d{3}-\d{4}')
	
	nums = phone_regexes.findall(text)
	return nums
		
def read_file():
	textcontent = ""
	while not textcontent:
		textfilepath = input('\nEnter file path for text file: ')
		try:
			textfile = open(textfilepath)
			textcontent = textfile.read()
			textfile.close()
			return textcontent
		except:
			print('\nIncorrect file path. Try again.')
		
def main():	
	print('\nThis program scans text files and prints out found phone numbers.\n')
	file = read_file()
	numbers = isPhoneNumber(file)
	print(numbers)
	
main()	