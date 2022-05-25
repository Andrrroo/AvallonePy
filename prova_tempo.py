import tkinter as tk
from guizero import *

def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

root = App()

label = tk.Label(root.tk, font=('Helvetica', 48), fg= 'white')
label.place(x=35, y=15)

# call countdown first time    
timer = PushButton(root, command= countdown(120))
# root.after(0, countdown, 5)

root.mainloop()