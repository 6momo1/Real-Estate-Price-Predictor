from selenium.webdriver.common.by import By
from bfs import Utils
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper:

	def scrapeRew(self, area: str,city: str,page: int) -> None:
		print("Scraping..")

		# this line disables css and blocks images from loading

		# initiate web driver object
		options = webdriver.ChromeOptions()

		# add arguments to the web driver
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



		# change the web driver proxy
		# PROXY = "95.111.230.142:3128" # IP:PORT or HOST:PORT
		# options.add_argument('--proxy-server=%s' % PROXY)

		# apply the options to the driver
		driver = webdriver.Chrome(executable_path=r"./chromedriver.exe", options=options)

		# real estate URL to scrape
		url = f'https://www.rew.ca/properties/areas/{area}-{city}-bc/page/{page}'
		driver.get(url)

		# initiate data dictionary
		li = {}

		# assign elements from the main page to a variable
		elements = driver.find_elements_by_class_name('displaypanel-content')

		try:
			# for each element in elements
			# for i in range(len(elements)):
			for i in range(1):

				try:
					# try to load the main page that displays all real estate listing for that page

					# wait for the card element to appear
					cards = WebDriverWait(driver, 10).until(
						EC.presence_of_all_elements_located((By.CLASS_NAME, 'displaypanel-content')
						)
					) 

					# select the i'th card element and click it
					element = driver.find_elements_by_class_name('displaypanel-content')
					element[i].click()

				except:
					print(
						f'[ERROR] Failed to load main page for area: {area.upper()} in city: {city.upper()} for page: {page}'
					)

				try:
					# wait for new page to load or wait until class name of "propertyheader-address" appears
					loaded = WebDriverWait(driver, 10).until(
						EC.presence_of_all_elements_located((By.CLASS_NAME, 'listingheader-address')
						)
					)

					try:
						# scrape the data from the page

						data = Utils().get_info(driver.page_source)

					except Exception as e:
						print("[ERROR EXCEPTION]: ",e)
						print(
							f'[ERROR] Failed to scrape data from element number {i} for area: {area.upper()} in city: {city.upper()} in page: {page}'
						)

					# Return to the main page with the list of elements
					driver.back()

				except:
					print(
						f'[ERROR] Failed to load information page for element number {i} from area:{area.upper()} in city: {city.upper()} in page: {page}'
					)

		except:
			print(f'[ERROR] Failed to main page for area: {area.upper()} city: {city.upper()} in page: {page}')

		# driver.quit()
