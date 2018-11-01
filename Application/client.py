from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
sys.path.append("../database")
import MyDB

def new_user_function(*args):
	pass
def new_user_function_popup(*args):
	"""This will open a pop up window for adding new users"""
	user_popup = Toplevel()
	user_popup.title("Create New user")
	
	new_email = ttk.Label(user_popup, text = "Enter Email ID").grid(column = 0, row = 0, sticky = E)
	new_password = ttk.Label(user_popup, text = "New Password").grid(column = 0, row = 1, sticky = E)
	confirm_password = ttk.Label(user_popup, text = "Confirm Password").grid(column = 0, row = 2, sticky = E)

	email = StringVar()
	password = StringVar()
	confirm_pass = StringVar()

	ttk.Entry(user_popup, width = 25, textvariable = email).grid(column = 1, row = 0, sticky = (E,W))
	ttk.Entry(user_popup, width = 25, textvariable = password).grid(column = 1, row = 1, sticky = (E,W))
	ttk.Entry(user_popup, width = 25, textvariable = confirm_pass).grid(column = 1, row = 2, sticky = (E,W))

	ttk.Button(user_popup, text = 'Create', command = new_user_function).grid(column = 1, row = 3, sticky = (E,W))


def authenticate_user(*args):
	"""Add code to take the entry field data and 
	authenticate with the server"""
	pass

def upload_function(*args):
	"""Add code to upload the given file to the server"""
	pass

def save_results(*args):
	"""Add code to save the file in the given folder"""
	pass

def browse_function(*args):
	"""Code to open a browse pop up to select file to be uploaded"""
	upload_fp.set(filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("Python Files","*.py"),("CPP files","*.cpp"),("All files","*.*"))))

def browse_destination(*args):
	"""Code to open browse pop up to select destination folder"""
	save_fp.set(filedialog.askdirectory())

def red_text(event=None):
    new_user.config(foreground = "red")

def black_text(event=None):
    new_user.config(foreground = "black")

root = Tk()
root.title("Chop-out: Client Application")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

user_id = StringVar()
password = StringVar()
upload_fp = StringVar()
save_fp = StringVar()

new_user = ttk.Label(mainframe, text = 'New User?')
new_user.grid(column = 2, row = 0, sticky = (E,W))
new_user.bind('<Button-1>',new_user_function_popup)
new_user.bind('<Enter>',red_text)
new_user.bind('<Leave>',black_text)

ttk.Label(mainframe, text = 'User').grid(column = 0, row = 0, sticky = E)
ttk.Label(mainframe, text = 'Password').grid(column =0, row = 1, sticky = E)
ttk.Label(mainframe, text = 'Upload Function').grid(column = 0, row = 2, sticky = W, columnspan = 2)
ttk.Label(mainframe, text = 'Result Directory').grid(column = 0, row = 4, sticky = W, columnspan = 2)

id_entry = ttk.Entry(mainframe, width = 15, textvariable = user_id)
id_entry.grid(column = 1, row = 0, sticky = (W, E))

pass_entry = ttk.Entry(mainframe, width = 15, textvariable = password)
pass_entry.grid(column = 1, row = 1, sticky = (W, E))

ttk.Button(mainframe, text = 'Browse', command = browse_function).grid(column = 0, row = 3, sticky = (E, W))

upload_fp_entry = ttk.Entry(mainframe, width = 15, textvariable = upload_fp)
upload_fp_entry.grid(column = 1, row = 3, sticky = (W, E))

ttk.Button(mainframe, text = 'Browse', command = browse_destination).grid(column = 0, row = 5, sticky = (E, W))

save_fp_entry = ttk.Entry(mainframe, width = 15, textvariable = save_fp)
save_fp_entry.grid(column = 1, row = 5, sticky = (W, E))

ttk.Button(mainframe, text = 'Login', command = authenticate_user).grid(column = 2, row = 1, sticky = (E, W))
ttk.Button(mainframe, text = 'Upload', command = upload_function).grid(column = 2, row = 3, sticky = (E, W))
ttk.Button(mainframe, text = 'Save', command = save_results).grid(column = 2, row = 5, sticky = (E, W))

for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)

root.mainloop()