#!/usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import messagebox

class ClientApp(tk.Tk):
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

if __name__=='__main__':
	app = ClientApp()
	app.mainloop()
