# Task 1
# tkinter is access for graphics user interface
import tkinter as tk

# strtime is use format time
from time import strftime

#create a object 
root = tk.Tk()

# adding title in output
root.title("Digital Clock")

# define time function
def time():

    # accessing a real time
    String = strftime("%H:%M:%S %p \n %A")
    
    # asign text varable to string
    label.config(text = String)

    #Show correct time
    label.after(1000,time)

# font , size , background colour , forground colour
label = tk.Label(root , font =( 'Times New Roman', 40), background= "white" ,foreground= "Red")

#alingment center
label.pack(anchor="center")

# call function
time()

# method of tkinter for wait user input
root.mainloop()