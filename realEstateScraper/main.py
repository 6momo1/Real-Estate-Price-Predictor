from rewScraper import Scraper
from bfs import Utils

# Interface
# running = True

# while running:
# 	area = input("Enter area: ").split(',')
# 	city = input('Enter city: ')
# 	pages = int(input("how many pages would you like to scrape?"))

# 	for a in area:
# 		for p in range(1,pages+1):
# 			try:
# 				Scraper().scrapeRew(a,city,p)
# 			except:
# 				pass

# 	keep_running = input("Would you like to pass? (y/n)")
# 	if keep_running == 'n':
# 		running = False


# test Scraper().scrapeRew() function
Scraper().scrapeRew('arbutus','vancouver', 1)


# # test Utils().get_info() function
# html = open('./rew_page.html', 'r')
# data = Utils().get_info(html.read())
# print(data)