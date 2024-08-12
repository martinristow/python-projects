from tkinter import *


def button_clicked():
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label!", font=("Arial", 15, "normal"))
# my_label.pack(side="left")
# my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="Hello")
# my_label.place(x=100, y=200)
# Grid is the easiest ways of visualizing and creating the layout
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
# button.pack()
# button.place(x=100, y=250)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=2, row=2)

# NOTICE -----------------
# cannot use geometry manager pack inside . which already has slaves managed by grid
# Grid is the easiest ways of visualizing and creating the layout
# Often i will choose Grid in my projects because it's just more flexible and more easy to understand
# ------------------------

window.mainloop()
