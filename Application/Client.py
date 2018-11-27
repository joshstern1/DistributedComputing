#!/usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class ClientApp(tk.Tk):
	"""This is the main application class"""
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight =1)
		container.grid_columnconfigure(0, weight =1)
		
		self.frames = {}
		frame = StartPage(container,self)
		self.frames[StartPage] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.show_frame(StartPage)

	def show_frame(self, container):
		frame = self.frames[container]
		frame.tkraise()

class StartPage(tk.Frame):
	"""The start page of the application is specified in this class"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		user_id = StringVar()
		password = StringVar()
		confirm_pass = StringVar()
		
		new_user = tk.Label(self, text = 'New User?')
		
		new_user.grid(column = 2, row = 0, sticky = "ew")
		new_user.bind('<Button-1>',new_user_function_popup)
		new_user.bind('<Enter>',red_text)
		new_user.bind('<Leave>',black_text)

		tk.Label(self, text = 'User').grid(column = 0, row = 0, sticky = "e")
		tk.Label(self, text = 'Password').grid(column =0, row = 1, sticky = "e")

		id_entry = tk.Entry(self, width = 15, textvariable = user_id)
		id_entry.grid(column = 1, row = 0, sticky = "ew")

		pass_entry = tk.Entry(self, width = 15, textvariable = password, show = "*")
		pass_entry.grid(column = 1, row = 1, sticky = "ew")

		tk.Button(self, text = 'Login', command = authenticate_user).grid(column = 2, row = 1, sticky = (E, W))
if __name__=='__main__':
	app = ClientApp()
	app.mainloop()
