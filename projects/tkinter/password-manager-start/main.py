from tkinter import *  # import all classes and constants
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email_username} \nPassword: {password}"
                                                              f" \nIs it ok to save ?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
            clear()


def clear():
    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=350, height=350)


# Logo Name
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website Input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


# Email/Username Input
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "martinristov084@gmail.com")

# Password Input
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Generate Password Button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
