import random
from tkinter import *

root=Tk()
root.title("Rolling dice Programme")
root.geometry("500x700")
label=Label(root,text='',font=("times",260))

def roll():
    dice=['\u2684','\u2685','\u2686','\u2687','\u2688','\u2689']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button=Button(root,text="Roll !",width=40,height=5,font=10,bg="white",bd=2,command=roll)
button.place(x=250,y=0)
root.mainloop()
