from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
#from se import pw

keyboard = Controller()

class TwitFollow:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome()
		self.username = username
		self.driver.get("https://www.twitter.com/login")
		sleep(2)
		keyboard.type(username)
		sleep(1)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		sleep(1)
		keyboard.type(pw)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(4)

	def followuser(self,username2):
		self.driver.get(username2)
		i = 0
		for i in range(19):
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
			sleep(0.2)
			i = i +1
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		
pw = 'thisisatest'
finduser = "ArianaGrande"
URL = "https://www.twitter.com/" + finduser
my_bot = TwitFollow("Testie75425216", pw)
my_bot.followuser(URL)
