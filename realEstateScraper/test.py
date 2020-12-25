
import time
import requests
from bs4 import BeautifulSoup
import json
import re
import mysql.connector



def table(token):
	try:
		pass
	except Exception as e:
		print(e)

url = "https://www.rew.ca/properties/areas/arbutus-vancouver-bc"
headers = {'User-Agent':"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
req = requests.get(url, headers = headers)
soup = BeautifulSoup(req.content, 'html.parser')

class Scrape:

	def getSoup(self, url):

		headers = {'User-Agent':"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
		req = requests.get(url, headers = headers)
		soup = BeautifulSoup(req.content, 'html.parser')

		return soup

	


file = open('rewPage.html')
soup = BeautifulSoup(file, 'html.parser')

cards = soup.find_all("div", attrs = {'class':"displaypanel-content"})

card = cards[0]

# prints the price
price = card.find_all("div", attrs = {'class':"displaypanel-title hidden-xs"})

# returns the content
content = card.find_all("div", attrs = {'class':"displaypanel-section clearfix"})

# returns the adress
address = card.find_all("div", attrs = {'class':"displaypanel-section"})

a = address[0].text.split('\n')[1]

info = []
info.append(price[0].text.strip('\n'))
info.append(a)


for i in content[0].find_all('li'):
	if ('bd') in i.text:
		info.append(int(i.text[0:1]))
	elif ('ba') in i.text:
		info.append(int(i.text[0:1]))
	else:
		info.append(i.text)

print(info)