import turtle as trtl
import tkinter as tk


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


def collect():
  user = name.get()
  name.delete(0, 'end')
  if user.lower() == "yes":
    name_t.clear()
    name_t.pencolor("magenta")
    name_t.write("WEEEEEEEEE!!!!", align = "center", font = ("Arial", 20, "bold"))
    do_stuff()
    name_t.clear()
    name_t.pencolor("yellow")
    name_t.write("Again?", align = "center", font = ("Arial", 20, "bold"))
  else:
    name_t.clear()
    name_t.pencolor("cyan")
    name_t.write("OK! No spin!", align = "center", font = ("Arial", 40, "bold"))
  
  
def changebg():
  color = usercolor.get()
  wn.bgcolor(color)
  
wn = trtl.Screen()
wn.bgcolor("grey")

name_t = trtl.Turtle()
name_t.pu()
name_t.hideturtle()
name_t.goto(-0, 100)
name_t.pencolor("white")
name_t.write("Enter 'yes' to see the turtle spin!", align = "center", font = ("Arial", 15, "bold"))

canvas = wn.getcanvas()
canvas2 = wn.getcanvas()
button = tk.Button(canvas.master, text="Press me!", command=collect)

username = ""
name = tk.Entry(canvas.master, textvariable=username)

button2 = tk.Button(canvas2.master, text="ChangeBg?", command=changebg)
usercolor = tk.Entry(canvas2.master)


canvas.create_window(-100, -180, window=button)
canvas.create_window(40, -180, window=name)

canvas2.create_window(-100, 180, window=button2)
canvas2.create_window(40, 180, window=usercolor)
canvas.create_window(40, -180, window=name)

my_lovely_turtle = trtl.Turtle(shape="turtle")
my_lovely_turtle.shapesize(6)

wn.mainloop()