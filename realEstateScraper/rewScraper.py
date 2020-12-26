import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bfs import get_info


PATH = './chromedriver.exe'

area = 'kitsilano'
city = 'vancouver'
page = 2
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.
url = 'https://www.rew.ca/properties/areas/{area}-{city}-bc/page/{page}'.format(area=area,city=city,page=page)
li = []

driver.get(url)

elements = driver.find_elements_by_class_name('displaypanel-content')

try:
	for i in range(len(elements)):
		driver.find_elements_by_class_name('displaypanel-content')[i].click()
		li.append(get_info(driver.page_source))
		driver.back()
		time.sleep(3)
except:
	print(li)

print('')

print(len(li))
print(li)
