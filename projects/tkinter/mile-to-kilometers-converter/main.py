from tkinter import *

CONVERSION_FACTOR = 0.62137119


def button_clicked():

    if miles_input.get().isnumeric():
        get_miles = float(miles_input.get())
        km = round(get_miles / CONVERSION_FACTOR, 4)
        kilometer_result_label.config(text=km)
    else:
        kilometer_result_label.config(text="Only numbers")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=150, pady=150)
window.minsize(width=500, height=300)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
