#Simple program that searches through text files and identifies phone numbers.

import sys
import re

def isPhoneNumber(text):
	#regex for phone numbers
	phone_regexes = re.compile(r'\d{3}[.\-]\d{3}[.\-]\d{4}') #normal domestic number
	phone_regexes_w_pre = re.compile(r'\d[.\-]\d{3}[.\-]\d{3}[.\-]\d{4}') #number with prefix
	phone_regexes_w_par = re.compile(r'\(\d{3}[\).\-]\d{3}[.\-]\d{4}') #number with parenthesis in area code
	
	nums = phone_regexes.findall(text)
	nums.append(phone_regexes_w_pre.findall(text))
	nums.append(phone_regexes_w_par.findall(text))
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