import tkinter as tk
def check_entry_fields():
    id=e1.get()
    if len(id)==7 and id.isdigit():
        res.configure(text = str(e1.get()+" is valid ID "))
    else:
        res.configure(text = str(e1.get()+" is not valid ID "))
master = tk.Tk()
master.geometry("420x120")
tk.Label(master, text="Id : ").pack()
e1 = tk.Entry(master)
e1.pack()
res = tk.Label(master)
res.pack()
tk.Button(master, text='Check', command=check_entry_fields).pack()
tk.mainloop()
