from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label!", font=("Arial", 15, "normal"))
# my_label.pack(side="left")
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="Hello")


def button_clicked():
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click me", command=button_clicked)
# button.pack(side="left")
button.pack()

# Entry
input = Entry(width=10)
input.pack()


window.mainloop()
