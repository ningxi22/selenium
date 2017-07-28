from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Restaurants-g60763-zfn29504-New_York_City_New_York.html#EATERY_OVERVIEW_BOX")

csv_file = open('reviews.csv','w')
writer = csv.writer(csv_file) 
writer.writerow(['name', 'stars', 'num_reviews', 'price', 'cuisine'])

while True:
	try:
		# i = 1
		# while i <= 30:
		# 	if i == 1:
		# 		resindex=('.//div[@id="EATERY_SEARCH_RESULTS"]//div[@class="listing rebrand listingIndex-1 first]')
		# 	else:                       
		# 		resindex=('.//div[@id="EATERY_SEARCH_RESULTS"]//div[@class="listing rebrand listingIndex-' + str(i)+']')
		# 		print(resindex)
		# 		i += 1 
		# print('='*50)
		
		#reviews = driver.find_elements_by_xpath(resindex)
		reviews = driver.find_elements_by_xpath('.//div[@id="EATERY_SEARCH_RESULTS"]//div[@data-index]')
		#patterns = ['.//span[@class="ui_bubble_rating bubble_45"]','.//span[@class="ui_bubble_rating bubble_40"]']
		for review in reviews:
			review_dict = {}
			
		#	for pattern in patterns:
		#		stars = review.find_element_by_xpath(pattern).get_attribute('alt')
		#		if stars:
		#			break
		#		else:
		#			stars = []
			name = review.find_element_by_xpath('.//a[@class="property_title"]').text
			stars = review.find_element_by_xpath('.//div[@class="rating rebrand"]/span').get_attribute('alt')
			num_reviews = review.find_element_by_xpath('.//span[@class="reviewCount"]').text
			#try:
			#	price = review.find_element_by_xpath('.//"]')
			#except Exception:
			#	price = ['']
			#try:
			#	cuisine = review.find_element_by_xpath('')

			review_dict['name'] = name
			review_dict['stars'] = stars
			review_dict['num_reviews'] = num_reviews
			#review_dict['price'] = price
			#review_dict['cuisine'] = cuisine
			writer.writerow(review_dict.values())

		button = driver.find_element_by_xpath('//a[@class="nav next rndBtn ui_button primary taLnk"]')
		button.click()
		time.sleep(2)
	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break


	# Better solution using Explicit Waits in selenium: http://selenium-python.readthedocs.io/waits.html?highlight=element_to_be_selected#explicit-waits

	# try:
	# 	wait_review = WebDriverWait(driver, 10)
	# 	reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
	# 								'//ol[@class="bv-content-list bv-content-list-Reviews bv-focusable"]/li')))
	# 	print(index)
	# 	print('review ok')
	# 	# reviews = driver.find_elements_by_xpath('//ol[@class="bv-content-list bv-content-list-Reviews bv-focusable"]/li')
	#
	# 	wait_button = WebDriverWait(driver, 10)
	# 	button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
	# 								'//div[@class="bv-content-list-container"]//span[@class="bv-content-btn-pages-next"]')))
	# 	print('button ok')
	# 	# button = driver.find_element_by_xpath('//span[@class="bv-content-btn-pages-next"]')
	# 	button.click()
	# except Exception as e:
	# 	print(e)
	# 	driver.close()
	# 	break
