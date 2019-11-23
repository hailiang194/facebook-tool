from selenium import webdriver
from tqdm import tqdm
from post import *

import time


def get_limit_posts():
	limit = str(input("Limit posts(all for get a posts)> "))

	if(limit.upper() == 'A'):
		return limit.upper()
	if(limit.isdigit()):
		return int(limit)

	return None

def is_posts_enough(posts, limit):
	if(limit == 'A'):
		return False

	return (len(posts) >= limit)

def get_all_posts(driver, link):

	limit = get_limit_posts()
	while(limit is None):
		limit = get_limit_posts()

	print('GOING TO %s' %(link))
	driver.get(link)

	print('GETTING ALL TARGET POST...')
	print('THIS MAY TAKE A WHILE ')

	while True:

		posts = driver.find_elements_by_css_selector("._5pcr.userContentWrapper")

		if(is_posts_enough(posts, limit)):
			break

		driver.execute_script("window.scrollTo(0, window.scrollMaxY)")
        	#loading
		start = int(time.time())
		while(int(time.time()) - start <= 40):
                	#check if scroll till bottom or not
			y = driver.execute_script("return window.scrollY")
			maxY = driver.execute_script("return window.scrollMaxY")

			if(y < maxY):
				break

			if(is_posts_enough(posts, limit)):
				break

		if(y == maxY):
			break

	if(limit == 'A'):
		limit = len(posts)
	elif(limit is None):
		limit = 0

	return [FBPost(post) for post in posts[:min(limit, len(posts))]]


def auto_like(driver):
	link = str(input("Link target> "))

	posts = get_all_posts(driver, link)

	if(len(posts) == 0):
		print("NO POST FOUND!")
		quit()

	print("TOTAL %d POST(S)" %(len(posts)))
	choise = input("DO YOU WANT TO LIKE ALL POST THAT HAVEN\'T BEEN LIKED? (Y/N)")

	if(choise.upper() == 'Y'):
		for post in tqdm(posts, desc = "Liking..."):
			post.get_react().like(driver)


