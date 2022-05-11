import tkinter as tk
  
root=tk.Tk()
# setting the windows size
root.geometry("500x300")
find_var=tk.StringVar()
replace_var=tk.StringVar()
# creating a label for
# find using widget Label
find_label = tk.Label(root, text = 'Find:', font=('calibre',10, 'bold'))
# creating a entry for input
# find using widget Entry
find_entry = tk.Entry(root,textvariable = find_var, font=('calibre',10,'normal'))
# creating a label for replace
replace_label = tk.Label(root, text = 'Replace:', font = ('calibre',10,'bold'))
# creating a entry for replace
replace_entry=tk.Entry(root, textvariable = replace_var, font = ('calibre',10,'normal'), show = '*')
# creating a button using the widget
find_btn=tk.Button(root,text = 'Find' , width=10)
findAll_btn=tk.Button(root,text = 'Find All' , width=10)
replace_btn=tk.Button(root,text = 'Replace', width=10 )
replaceAll_btn=tk.Button(root,text = 'Replace All', width=10 )
# placing the label and entry in
# the required position using grid
# method
find_label.grid(row=0,column=0,sticky='e')
find_entry.grid(row=0,column=1,sticky='e')
replace_label.grid(row=1,column=0)
replace_entry.grid(row=1,column=1)
find_btn.grid(row=0,column=3)
findAll_btn.grid(row=1,column=3)
replace_btn.grid(row=2,column=3)
replaceAll_btn.grid(row=3,column=3)
  
# performing an infinite loop
# for the window to display
root.mainloop()