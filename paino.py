from tkinter import *
import pygame

def play_C(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\C.wav') # file path depends on where you place the file 
    sound.play()

    
def play_C_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\C_s.wav')
    sound.play()

def play_D(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\D.wav')
    sound.play()


def play_D_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\D_s.wav')
    sound.play()

def play_E(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\E.wav')
    sound.play()

def play_F(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\F.wav')
    sound.play()

def play_F_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\F_s.wav')
    sound.play()

def play_G(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\G.wav')
    sound.play()

def play_G_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\G_s.wav')
    sound.play()

def play_A(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\A.wav')
    sound.play()

def play_A_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\A_s.wav')
    sound.play()

def play_B(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('Music_Notes\B.wav')
    sound.play()


# main program
gui = Tk()           # make a GUI window
topframe = Frame(gui, width=20, height=5)
topframe.grid(column=0, row=0)
bottomframe = Frame(gui, width=20, height=15)
bottomframe.grid(column=0, row=1)


button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=0, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=2, row=0, columnspan=2, rowspan=3)


button2 = Button(bottomframe, width=2, height=7, bg='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=1, row=0, columnspan=2, rowspan=2)

button5 = Button(bottomframe, width=3, height=10, bg='ivory')
button5.bind('<Button-1>', play_E)
button5.grid(column=4, row=0, columnspan=2, rowspan=3)


button4 = Button(bottomframe, width=2, height=7, bg='black')
button4.bind('<Button-1>', play_D_sharp)
button4.grid(column=3, row=0, columnspan=2, rowspan=2)

button6 = Button(bottomframe, width=3, height=10, bg='ivory', )
button6.bind('<Button-1>', play_F)
button6.grid(column=6, row=0, columnspan=2, rowspan=3)

button7 = Button(bottomframe, width=3, height=10, bg='ivory')
button7.bind('<Button-1>', play_G)
button7.grid(column=8, row=0, columnspan=2, rowspan=3)


button7 = Button(bottomframe, width=2, height=7, bg='black')
button7.bind('<Button-1>', play_F_sharp)
button7.grid(column=7, row=0, columnspan=2, rowspan=2)

button9 = Button(bottomframe, width=3, height=10, bg='ivory')
button9.bind('<Button-1>', play_A)
button9.grid(column=10, row=0, columnspan=2, rowspan=3)


button8 = Button(bottomframe, width=2, height=7, bg='black')
button8.bind('<Button-1>', play_G_sharp)
button8.grid(column=9, row=0, columnspan=2, rowspan=2)

button11 = Button(bottomframe, width=3, height=10, bg='ivory')
button11.bind('<Button-1>', play_B)
button11.grid(column=12, row=0, columnspan=2, rowspan=3)


button10 = Button(bottomframe, width=2, height=7, bg='black')
button10.bind('<Button-1>', play_A_sharp)
button10.grid(column=11, row=0, columnspan=2, rowspan=2)

button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=14, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=16, row=0, columnspan=2, rowspan=3)


button2 = Button(bottomframe, width=2, height=7, bg='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=15, row=0, columnspan=2, rowspan=2)

button5 = Button(bottomframe, width=3, height=10, bg='ivory')
button5.bind('<Button-1>', play_E)
button5.grid(column=18, row=0, columnspan=2, rowspan=3)


button4 = Button(bottomframe, width=2, height=7, bg='black')
button4.bind('<Button-1>', play_D_sharp)
button4.grid(column=17, row=0, columnspan=2, rowspan=2)

button6 = Button(bottomframe, width=3, height=10, bg='ivory', )
button6.bind('<Button-1>', play_F)
button6.grid(column=20, row=0, columnspan=2, rowspan=3)

button7 = Button(bottomframe, width=3, height=10, bg='ivory')
button7.bind('<Button-1>', play_G)
button7.grid(column=22, row=0, columnspan=2, rowspan=3)


button7 = Button(bottomframe, width=2, height=7, bg='black')
button7.bind('<Button-1>', play_F_sharp)
button7.grid(column=21, row=0, columnspan=2, rowspan=2)

button9 = Button(bottomframe, width=3, height=10, bg='ivory')
button9.bind('<Button-1>', play_A)
button9.grid(column=24, row=0, columnspan=2, rowspan=3)


button8 = Button(bottomframe, width=2, height=7, bg='black')
button8.bind('<Button-1>', play_G_sharp)
button8.grid(column=23, row=0, columnspan=2, rowspan=2)

button11 = Button(bottomframe, width=3, height=10, bg='ivory')
button11.bind('<Button-1>', play_B)
button11.grid(column=26, row=0, columnspan=2, rowspan=3)


button10 = Button(bottomframe, width=2, height=7, bg='black')
button10.bind('<Button-1>', play_A_sharp)
button10.grid(column=25, row=0, columnspan=2, rowspan=2)


mainloop()