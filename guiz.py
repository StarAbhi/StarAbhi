from guizero import App, Drawing

a = App()

# create drawing object
d = Drawing(a, width=220, height=220)
d.rectangle(10, 10, 210, 210, color="light blue")
d.oval(30, 30, 50, 50, color="white", outline=True)
d.oval(170, 30, 190, 50, color="white", outline=True)
d.triangle(110, 90, 120, 110, 100, 110, color="black")
d.line(50, 180, 50, 160, color="red", width=5)
d.line(50, 180, 170, 180, color="red", width=5)
d.line(170, 180, 170, 160, color="red", width=5)

a.display()