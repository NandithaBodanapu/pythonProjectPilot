#this is a countdown python project using tkinter
#reference geeksforgeeks
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

root =Tk()
root.geometry("500x500")
root.title("Count Down App")
#variables for hr min and sec
vhr=StringVar()# for widget
vmin=StringVar()
vsec=StringVar()
#set the  time to zero
vhr.set("00")
vmin.set("00")
vsec.set("00")
#create the entry
hr_entry=ttk.Entry(root,textvariable=vhr)
hr_entry.grid(row=0,column=0)

min_entry=ttk.Entry(root,textvariable=vmin)
min_entry.grid(row=0,column=1)

sec_entry=ttk.Entry(root,textvariable=vsec)
sec_entry.grid(row=0,column=2)

def timecountdown():
    try:
        temp= int(vhr.get()) * 3600 + int(vmin.get()) * 60 + int(vsec.get())
    except:
        print("enter right elements")

    while temp>-1:
         mins,secs=divmod(temp,60)
         temp=temp-1
         hrs=0
         if mins>60:
           hrs,mins=divmod(mins,60)
         vhr.set(f"{hrs}")
         vmin.set(f"{mins}")
         vsec.set(f"{secs}")
         root.update()
         time.sleep(1)
         if temp==0:
            messagebox.showinfo("Countdown App","Time Exceeded")

sub_button=Button(root,text="countdown",command=timecountdown)
sub_button.grid(row=2,column=1)
root.mainloop()


