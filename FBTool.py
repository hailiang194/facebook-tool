#this program use seleium you have to install it
#in Python3 type command 'pip3 install selenium'
#it also use Firefox webdrive to operate it
#download at https://github.com/mozilla/geckodriver/releases/
#extract the file and move it to /usr/bin for ubuntu version

from selenium import webdriver
from login import *
from post import *
from tool import *

def exit_program(driver):
	driver.close()
	quit()

options = webdriver.FirefoxOptions()
options.set_preference('dom.push.enabled', False)
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_options = options)

if(not login_to_facebook(driver)):
	print('Login failed!')
	quit()
else:
	print('Login successfully!')

print('CHOOSE FUNCTION')
print('1. AUTO LIKE FACEBOOK')
print('OTHER: QUIT')
try:
	choice = int(input(">> "))
except:
	exit_program()

if(choice == 1):
	auto_like(driver)

driver.quit()
quit()
