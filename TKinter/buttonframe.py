import tkinter as tk
def pressed():
    print('Button is pressed')


def create_layout(frame: tk.Frame) -> None:
    # created the buttons
    # now time to pack them
    # creating a row in frame
    first_row = tk.Frame(frame)
    first_row.pack(side=tk.TOP, fill=tk.X, expand=True)
    second_row = tk.Frame(frame)
    second_row.pack(side=tk.TOP, fill=tk.X, expand=True)
    third_row = tk.Frame(frame)
    third_row.pack(side=tk.TOP, fill=tk.X, expand=True)

    # creating boxes
    box1 = tk.Frame(first_row)
    box1.pack(side=tk.LEFT, fill=tk.X, expand=True)
    box2 = tk.Frame(first_row)
    box2.pack(side=tk.LEFT, fill=tk.X, expand=True)
    box3 = tk.Frame(first_row)
    box3.pack(side=tk.LEFT, fill=tk.X, expand=True)
    button1 = tk.Button(box1, text="Button1", command=pressed)
    button1.pack(side=tk.LEFT)

    box4 = tk.Frame(second_row)
    box4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    box5 = tk.Frame(second_row)
    box5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    box6 = tk.Frame(second_row)
    box6.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    button4 = tk.Button(box6, text="Button4", command=pressed)
    button4.pack(side=tk.LEFT)

    button3 = tk.Button(box5, text="Button3", command=pressed)
    button3.pack(side=tk.LEFT)
    # populating the middle row

    box7 = tk.Frame(third_row)
    box7.pack(side=tk.LEFT, fill=tk.X, expand=True)
    box8 = tk.Frame(third_row)
    box8.pack(side=tk.LEFT, fill=tk.X, expand=True)
    box9 = tk.Frame(third_row)
    box9.pack(side=tk.LEFT, fill=tk.X, expand=True)

    button2 = tk.Button(box7, text="Button2", command=pressed)
    button2.pack(side=tk.LEFT)

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('400x200+20+20')
    frame = tk.Frame()
    frame.pack(expand=1, fill=tk.X)
    create_layout(frame)
    window.mainloop()