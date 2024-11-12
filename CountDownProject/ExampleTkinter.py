#examples for Tkinter

from tkinter  import *

#from click import command

root =Tk()
def  hello():
    text=Label(root,text="Hello World")# create a variable
    text.pack()#pack it


button_one=Button(root,fg="red",text="click",command=hello())
button_one.pack()
root.mainloop()# they are continually looping function