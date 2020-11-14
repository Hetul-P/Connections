import tkinter as tk
    

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
		
def run():
    pw = 'thisisatest'

    username = 'ryans_fire'
    my_bot = Follow('test.aaccc', pw)
    my_bot.followuser(username)


root = tk.Tk()

def show_entry_fields():
    print("User: %s\nPass: %s\nRequesting: %s" % (e1.get(), e2.get(), e3.get()))

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()


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

tk.Checkbutton(root, text = "Instagram", variable = a, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=0)
tk.Checkbutton(root, text = "Facebook", variable = b, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=1)
tk.Checkbutton(root, text = "Twitter", variable = c, onvalue = 1, offvalue = 0, height=5, width = 20).grid(row=5, column=2)
root.mainloop()

