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

		def red_text(event=None):
		    new_user.config(foreground = "red")

		def black_text(event=None):
		    new_user.config(foreground = "black")

		def new_user_function_popup(*args):
			"""This will open a pop up window for adding new users"""
			user_popup = Toplevel()
			user_popup.title("Create New user")

			tk.Label(user_popup, text = "Enter Email ID").grid(column = 0, row = 0, sticky = "e")
			tk.Label(user_popup, text = "New Password").grid(column = 0, row = 1, sticky = "e")
			tk.Label(user_popup, text = "Confirm Password").grid(column = 0, row = 2, sticky = "e")

			tk.Entry(user_popup, width = 25, textvariable = user_id).grid(column = 1, row = 0, sticky = "ew")
			tk.Entry(user_popup, width = 25, textvariable = password, show = "*").grid(column = 1, row = 1, sticky = "ew")
			tk.Entry(user_popup, width = 25, textvariable = confirm_pass, show = "*").grid(column = 1, row = 2, sticky = "ew")
			tk.Button(user_popup, text = 'Create', command = new_user_function).grid(column = 1, row = 3, sticky = "ew")

		def new_user_function(*args):
			if password.get() == confirm_pass.get():
				baseURL = 'http://' + IP_Add_Server + PORT
				postURL = baseURL + '/new-user'
				data = {'username': user_id.get(),'password': password.get()}
				r = requests.post(url = postURL, data = data)
				if r == False:
					messagebox.showinfo("Invalid username!")
				else:
					messagebox.showinfo("Profile created!!")
			else:
				messagebox.showinfo("Passwords don't match")

		def authenticate_user(*args):
			"""Add code to take the entry field data and 
			authenticate with the server"""
			baseURL = 'http://' + IP_Add_Server + PORT
			postURL = baseURL + '/authenticate'
			data = {'username': user_id.get(),'password': password.get()}
			check = requests.post(url = postURL, data = data)
			if check == None:
				messagebox.showinfo("Wrong Password. Please try again")
			else:
				controller.show_frame(UploadSelectionPage)

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

		tk.Button(self, text = 'Login', command = authenticate_user).grid(column = 2, row = 1, sticky = "ew")

class UploadSelectionPage(tk.Frame):
	"""This page asks the user to upload new function or select from the existing one"""
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		def browse_function(*args):
			"""Code to open a browse pop up to select file to be uploaded"""
			upload_fp.set(filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Python Files","*.py"),("CPP files","*.cpp"),("All files","*.*"))))

		upload_fp = StringVar()
		
		tk.Label(self, text = 'Upload Function').grid(column = 0, row = 0, sticky = "w", columnspan = 2)
		
		tk.Button(self, text = 'Browse', command = browse_function).grid(column = 0, row = 1, sticky = "ew")
		upload_fp_entry = tk.Entry(self, width = 15, textvariable = upload_fp).grid(column = 1, row = 1, sticky = "ew")
		Upload = tk.Button(self, text = 'Upload', command = upload_function).grid(column = 2, row = 1, sticky = "ew")

if __name__=='__main__':
	app = ClientApp()
	app.mainloop()
