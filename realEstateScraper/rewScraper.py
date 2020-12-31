from selenium.webdriver.common.by import By
from bfs import get_info
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapRew(area,city,page):

	# chrome_options = webdriver.ChromeOptions()
	# prefs = {"profile.managed_default_content_settings.images": 2}
	# chrome_options.add_experimental_option("prefs", prefs)
	# driver = webdriver.Chrome(chrome_options=chrome_options)

	# this code disables css and blocks images from loading
	options = webdriver.ChromeOptions()
	prefs = {'profile.default_content_setting_values': {'images': 2, 
	                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
	                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,'protocol_handlers': 2, 
	                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
	                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
	                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
	                            'durable_storage': 2}}
	options.add_experimental_option('prefs', prefs)
	options.add_argument("start-maximized")
	options.add_argument("disable-infobars")
	options.add_argument("--disable-extensions")


	# change the proxy of selenium
	PROXY = "95.111.230.142:3128" # IP:PORT or HOST:PORT
	options.add_argument('--proxy-server=%s' % PROXY)

	driver = webdriver.Chrome(chrome_options=options)


	url = f'https://www.rew.ca/properties/areas/{area}-{city}-bc/page/{page}'
	driver.get(url)

	li = {}
	elements = driver.find_elements_by_class_name('displaypanel-content')

	try:
		for i in range(len(elements)):

			try:
				# wait for the card element to appear
				cards = WebDriverWait(driver, 10).until(
					EC.presence_of_all_elements_located((By.CLASS_NAME, 'displaypanel-content')
					)
				) 

				# select card element
				element = driver.find_elements_by_class_name('displaypanel-content')
				element[i].click()

			except:
				print(
					f'Failed to load main page for area: {area.upper()} in city: {city.upper()} for page: {page}'
				)

			try:
				# wait for new page to load
				loaded = WebDriverWait(driver, 10).until(
					EC.presence_of_all_elements_located((By.CLASS_NAME, 'propertyheader-address')
					)
				)

				try:
					# scrape the data from the page
					get_info(driver.page_source)

				except:
					print(
						f'Failed to scrape data from element number {i} for area: {area.upper()} in city: {city.upper()} in page: {page}'
					)

				# go back to the main page with the list of elements
				driver.back()

			except:
				print(
					f'Failed to load information page for element number {i} from area:{area.upper()} in city: {city.upper()} in page: {page}'
				)

	except:
		print(f'Failed to main page for area: {area.upper()} city: {city.upper()} in page: {page}')

	driver.quit()
