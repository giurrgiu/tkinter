from tkinter import *
from tkinter import ttk

def submitForm(*args):
    pass
root=Tk()
root.title("Labels PlayGround")


test=StringVar()
image_test=PhotoImage(file="testbear.gif")

mainframe=ttk.Frame(root)
mainframe.grid(column=0,row=0,sticky=(S,W,E,N))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

label1=ttk.Label(mainframe,textvariable=test,background="red",font="Helvetica,42").grid()
labelphoto=ttk.Label(mainframe,image=image_test).grid()
label2=ttk.Label(mainframe,textvariable=test).grid()
label3=ttk.Label(mainframe,textvariable=test,image=image_test,compound="right").grid()

'''
button
'''

button=ttk.Button(mainframe,text="Button",command=submitForm).grid()


test.set("First Name:")

root.mainloop()
