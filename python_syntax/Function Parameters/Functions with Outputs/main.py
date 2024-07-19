# Functions with Outputs
def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
output = format_name("maRtin","ristov")
print(output)

# Multiple return values
def format_name_multiple_return(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Results: {formated_f_name} {formated_l_name}"
output = format_name(input("What is your first name:"),input("What is your last name:"))
print(output)