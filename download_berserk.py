# download_berserk.py - Downloads every single Berserk issue.
# Collects every image from each Berserk chapter from www.readberserk.com
# Parental Advisory: Berserk is a manga meant for adults with very dark themes along with nudity, 
#					 extreme gore and violence, and sexual content and is not recommended for children 
#					 or anyone with a weak stomach.

import requests, os, bs4, re

url = 'http://readberserk.com/chapter/berserk-chapter-a0/' #starting url

mainDir = "berserk"
os.makedirs(mainDir, exist_ok=True) #Store comics in ./berserk

while url != []:

	#Create subdirectory for chapter
	chapterDir = url.split('/') [-2]
	chapterDir = chapterDir.replace('berserk-', '')
	imgDir = os.path.join(mainDir, chapterDir)
	os.makedirs(imgDir, exist_ok=True)
	#Download the Page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text, features='html.parser')
	
	#Find URL of comic image.
	comicElem = soup.select('.pages__img')
	if comicElem == []:
		print('Could not find comic images.')
	else:
		print('Downloading %s...' % (chapterDir))
		
		# print(comicElem)
		# exit()
		
		for item in comicElem:
			comicUrl = item.get('src')
			# if comicUrl == []:
				# continue

			comicUrl = ''.join(comicUrl.partition('.jpg')[:2]) #cleans up junk after jpg extension
			comicUrl = ''.join(comicUrl.partition('.png')[:2])
			#print(comicUrl)
		
			#Download the image./
			try:
				res = requests.get(comicUrl)
				res.raise_for_status()
	
				#Save image to ./berserk/<chapter>
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
	
	
	
	#Get Next button's url
	if not soup.find("a", class_ = 'button button-primary', string = re.compile("^Next")):
		print('Next chapter unavailable')
		url = []
	else:
		nextLink = soup.find("a", class_ = 'button button-primary', string = re.compile("^Next"))
		url = nextLink.get('href')
	
	
print('Done.')