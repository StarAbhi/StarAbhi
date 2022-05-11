from tkinter import *
from tkinter import messagebox
from math import *
from functools import partial  

error1='Enter any one value plz'
error2='Delete any one value plz'

def calculate(temp1,temp2):
    celsius=temp1.get()
    fahrenheit =temp2.get()
    if(len(celsius)==0 and len(fahrenheit)==0):
        messagebox.showerror("error",error1)
    elif(len(celsius)==0 and len(fahrenheit) !=0):
        Ce=((float(fahrenheit)-32)*(5/9))
        C1='{:f}'.format(Ce)
        temp1.set(C1)
    elif(len(celsius)!=0 and len(fahrenheit)==0):
        F=((float(celsius)*9/5))+32
        F1='{:f}'.format(F)
        temp2.set(F1)
    elif(len(celsius)!=0 and len(fahrenheit)!=0):
        messagebox.showerror("error",error2)

root=Tk()
root.title('Temperature Conversion Calculator.')
root.geometry('440x100')
root.maxsize(440, 100)

temp1=StringVar()
temp2=StringVar()

l1=Label(root,text='Celsius').place(x=45,y=45)
t1=Entry(root,textvariable=temp1,width=15).place(x=40,y=25)

l2=Label(root,text='Fahrenheit').place(x=310,y=45)
t2=Entry(root,textvariable=temp2,width=15).place(x=300,y=25)

calculate = partial(calculate,temp1,temp2)
btn=Button(root,text='=',command=calculate,width=10).place(x=180,y=20)

root.mainloop()