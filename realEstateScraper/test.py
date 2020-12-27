from selenium.webdriver.common.by import By
from bfs import get_info
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapRew(area,city,page):

	# these lines of code block block images from loading in the driver
	opt = webdriver.ChromeOptions()
	opt.add_extension("Block-image_v1.1.crx")
	browser = webdriver.Chrome(chrome_options=opt)


	PATH = './chromedriver.exe'
	driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

	url = f'https://www.rew.ca/properties/areas/{area}-{city}-bc/page/{page}'

	driver.get(url)

	li = {}

	elements = driver.find_elements_by_class_name('displaypanel-content')

	try:
		for i in range(len(elements)):

			try:
				cards = WebDriverWait(driver, 10).until(
					EC.presence_of_all_elements_located((By.CLASS_NAME, 'displaypanel-content')
					)
				) 
				element = driver.find_elements_by_class_name('displaypanel-content')
				element[i].click()
			except Exception as e:
				print(e)

			try:
				loaded = WebDriverWait(driver, 10).until(
					EC.presence_of_all_elements_located((By.CLASS_NAME, 'propertyheader-address')
					)
				) 
				try:
					get_info(driver.page_source)
				except:
					pass
				driver.back()

			except Exception as e:
				print(e)
	except:
		pass
	driver.quit()