# 1st of all importing modules
from tkinter import ttk
from tkinter import *

# Making window
root = Tk()
# Give window Title
root.title("Progressbar")
# Give window geometry
root.geometry("300x45")
# Making Progressbar
ProgressBar = ttk.Progressbar(root, orient="horizontal", length=300, maximum=100, mode="determinate")
# pack the Progressbar
ProgressBar.pack()
# Making Label
Label = Label(root, text="In Process")
# pack Label
Label.pack()
#  take a variable
loading = 0
# Making Function
def update():
    # take global variable
    global loading
    # increasing global variable
    loading += 1
    # put the value in ProgressBar
    ProgressBar['value'] = loading
    if ProgressBar['value'] >= ProgressBar['maximum']:
        Label['text'] = "The Process is done!"
    #     Stopping Processing using after function
    root.after(100, update)


update()

root.mainloop()
