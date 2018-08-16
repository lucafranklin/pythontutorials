# download_onepunch.py - Downloads every single One Punch Man issue.
# Collects every image from each One Punch Man chapter from http://read3.watchopm.net

import requests, os, bs4, re

url = 'http://read3.watchopm.net/one-punch-man-chapter-001/' #starting url

mainDir = "one_punch_man"
os.makedirs(mainDir, exist_ok=True) #Store comics in ./one_punch_man

while url != []:

	#Create subdirectory for chapter
	chapterDir = url.split('/') [-2]
	chapterDir = chapterDir.replace('one_punch_man-', '')
	imgDir = os.path.join(mainDir, chapterDir)
	os.makedirs(imgDir, exist_ok=True)
	#Download the Page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text, features='html.parser')
	
	#Find URL of comic images.
	comicElem = soup.find_all('img')
	# for elem in comicElem:
		# print(elem)
	# exit()
	
	if comicElem == []:
		print('Could not find comic images.')
	else:
		print('Downloading %s...' % (chapterDir))
		
		# print(comicElem)
		# exit()
		
		for item in comicElem:
			comicUrl = item.get('src')
			if not comicUrl:
				continue

			comicUrl = ''.join(comicUrl.partition('.jpg')[:2]) #cleans up junk after jpg extension
			comicUrl = ''.join(comicUrl.partition('.png')[:2])
			#print(comicUrl)
		
			#Download the image./
			try:
				res = requests.get(comicUrl)
				res.raise_for_status()
	
				#Save image to ./one_punch_man/<chapter>
				# if comicElem.index(item) != len(comicElem)-1:
				# comicUrl = comicUrl[:-1] #removes '/r' left over on url for everything but the last comic
			
				fileName = os.path.basename(comicUrl)
				fileName = fileName[-12:]
			
				imageFile = open(os.path.join(imgDir, fileName), 'wb')
				
				#imageFile = open(os.path.join(imgDir, str(comicElem.index(item)+1) + '.jpg'), 'wb')
				#print(imageFile)
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
				imageFile.close()
			except:
				print('Unable to download %s' % (os.path.basename(comicUrl)))
				print('Unable to save %s' % (fileName))
	
	
	
	#exit()
	
	#Get Next button's url
	if not soup.find("a", class_ = 'next page-numbers'):
		print('Next chapter unavailable')
		url = []
	else:
		nextLink = soup.find("a", class_ = 'next page-numbers')
		url = nextLink.get('href')
	
	
print('Done.')