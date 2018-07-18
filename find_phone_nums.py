#Simple program that searches through text files and identifies phone numbers.

import sys
import re

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range (0,3):
		if not text[i].is_decimal:
			return False
	if text[3] != '-':
		return False
	for i in range (4,7):
		if not text[i].is_decimal:
			return False
	if text[7] != '-':
		return False
	for i in range (8,12):
		if not text[i].is_decimal:
			return False
	else:
		return True
		
def read_file():
	while True:
		textfilepath = input('\nEnter file path for text file: ')
		try:
			textfile = open(textfilepath)
			textcontent = textfile.read()
			textfile.close()
			return textcontent
		except:
			print('Incorrect file path. Try again.\n')
		
def main():
	
	numbers = []
	
	print('\nThis program scans text files and prints out found phone numbers.\n')
	file = read_file()
	file.replace("\n", " ")
	wordlist = file.split(" ")
	for word in wordlist:
		if isPhoneNumber(word):
			numbers.append(word)
		else:
			continue
	print numbers
	
main()	