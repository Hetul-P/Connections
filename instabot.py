from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

class Follow:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome()
		self.username = username
		self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(4)
	def followuser(self,username2):
		self.driver.get("https://www.instagram.com/"+username2+"/")
		sleep(4)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		
		
pw = 'thisisatest'

username = 'ryans_fire'
my_bot = Follow('test.aaccc', pw)
my_bot.followuser(username)
