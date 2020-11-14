import tkinter as tk
from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
from itertools import islice

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

class IGFollow:
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
		self.driver.get(username2)
		sleep(4)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

def run():
	user = e1.get()
	pw = e2.get()
	my =[]
	igfollower = []
	fbfollower = []
	twfollower = []
	with open("storage.txt", "r") as fin:
		for line in islice(fin,0,4):
			line = line.split()
			if(line[1] == user):
				if(line[2] == pw):
					for i in range(0,12):
						my.append(line[i])

	if ig.get() == 1:
		my_igbot = IGFollow(my[3], my[4])
		with open("storage.txt", "r") as fin:
			for follow in islice(fin,0,4):
				follow = follow.split()
				if(follow[1] == e3.get()):
					for i in range(0,12):
						igfollower.append(follow[i])
		if(igfollower[5]!= 'blank'):
			my_igbot.followuser(igfollower[5])

	if fb.get() == 1:
		my_fbbot = FBReq(my[6],my[7])
		with open("storage.txt", "r") as fin:
			for follow in islice(fin,0,4):
				follow = follow.split()
				if(follow[1] == e3.get()):
					for i in range(0,12):
						fbfollower.append(follow[i])
		if(fbfollower[8]!= 'blank'):
			my_fbbot.sendreq(fbfollower[8])

	if tw.get()== 1:
		my_twbot = TwitFollow(my[9],my[10])
		with open("storage.txt", "r") as fin:
			for follow in islice(fin,0,4):
				follow = follow.split()
				if(follow[1] == e3.get()):
					for i in range(0,12):
						twfollower.append(follow[i])
		if(twfollower[11]!= 'blank'):
			my_twbot.followuser(twfollower[11])


if __name__ == "__main__":

	root = tk.Tk()

	def show_entry_fields():
		print("User: %s\nPass: %s\nRequesting: %s" % (e1.get(), e2.get(), e3.get()))

	ig = tk.IntVar()
	fb = tk.IntVar()
	tw = tk.IntVar()


	button = tk.Button(
					   text="QUIT", 
					   fg="red",
					   command=quit)
	button.grid(row=4, column=0)
	slogan = tk.Button(
						text="Request Friend",
					   command=run)
	slogan.grid(row=4,column=1)

	tk.Label(root, text="Username:").grid(row=0)
	tk.Label(root, text="Password:").grid(row=1)
	tk.Label(root, text="Search for:").grid(row=2)

	e1 = tk.Entry(root)
	e2 = tk.Entry(root)
	e3 = tk.Entry(root)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)

	tk.Button(root, text='Show', command=show_entry_fields).grid(row=4, column=2)
	tk.Button(root, text='Create Account', command=show_entry_fields).grid(row=1, column=2)
	tk.Button(root, text='Facebook', command=show_entry_fields).grid(row=5, column=1)
	tk.Button(root, text='Twitter', command=show_entry_fields).grid(row=5, column=2)

	tk.Checkbutton(root, text = "Instagram", variable = ig, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=0)
	tk.Checkbutton(root, text = "Facebook", variable = fb, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=1)
	tk.Checkbutton(root, text = "Twitter", variable = tw, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=2)



	root.mainloop()