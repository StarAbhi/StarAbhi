from tkinter import *

def show_textbox_msg():
    text_box.insert(END,"\n Be happy for this moment. This moment is your life.")
def clear_textbox_msg():
    text_box.delete(1.0, 'end')

win = Tk()
win.title('textBox')
win.geometry('400x400')
win.config(bg='#84BF04')

message ='''Dear Reader, Here is some text for you...!!!  '''

text_box = Text(
    win,
    height=15,
    width=50
)
text_box.pack(expand=True)
text_box.insert('end', message)

Button(
    win,
    text='Clear',
    width=15,
    height=2,
    command=clear_textbox_msg
).pack(expand=True)
Button(
    win,
    text='Show',
    width=15,
    height=2,
    command=show_textbox_msg
).pack(expand=True)

win.mainloop()