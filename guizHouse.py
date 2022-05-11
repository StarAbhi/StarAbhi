from guizero import App, Drawing

a = App()

# create drawing object
d = Drawing(a, width=220, height=220)
d.rectangle(10, 110, 210, 250,outline_color="black", color="light blue")
d.triangle(110, 10, 210, 110, 10, 110,outline_color="black", color="pink")
d.rectangle(80, 150, 140, 250,outline_color="black", color="yellow")
d.rectangle(30, 150, 140, 250,outline_color="black", color="blue")
d.line(80, 80, 120, 120, color="black", width=1)
a.display()