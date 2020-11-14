from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
#from se import pw

keyboard = Controller()

class FBReq:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome()
		self.username = username
		self.driver.get("https://www.facebook.com/login")
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
		
	def sendreq(self,username2):
		self.driver.get(username2)
		i = 0

		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		sleep(0.1)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		for i in range(16):
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
			sleep(0.2)
			i = i +1
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

		
pw = 'thisisatest'
finduser = "hetul.patel.712"
URL = "https://www.facebook.com/" + finduser
my_bot = FBReq("a.t.es.tatat@gmail.com", pw)
my_bot.sendreq(URL)
