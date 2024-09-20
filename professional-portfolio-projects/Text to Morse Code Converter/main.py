morse_code = {
        "A": "._",
        "N": "_.",
        "B": "_...",
        "O": "___",
        "C": "_._.",
        "P": ".__.",
        "D": "_..",
        "Q": "__._",
        "E": ".",
        "R": "._.",
        "F": ".._.",
        "S": "...",
        "G": "__.",
        "T": "_",
        "H": "....",
        "U": ".._",
        "I": "..",
        "V": "..._",
        "J": ".___",
        "W": ".__",
        "K": "_._",
        "X": "_.._",
        "L": "._..",
        "Y": "_.__",
        "M": "__",
        "Z": "__..",
        "1": ".____",
        "6": "_....",
        "2": "..___",
        "7": "__...",
        "3": "...__",
        "8": "___..",
        "4": "...._",
        "9": "____.",
        "5": ".....",
        "0": "_____",
        " ": "/",
        "?": "..__..",
        ";": "_._._.",
        ":": "___...",
        "/": "_.._.",
        "-": "_...._",
        "\'": ".____.",
        "\"": "._.._.",
        "(": "_.__.",
        ")": "_.__._",
        "=": "_..._",
        "+": "._._.",
        "*": "_.._",
        "@": ".__._.",
        "Á": ".__._",
        "Ä": "._._",
        "É": ".._..",
        "Ñ": "__.__",
        "Ö": "___.",
        "Ü": "..__",
        ".": " "}


def morse_code_fun(text):
    if text == "" or len(text) <= 3:
        print("You must enter text greater than 3 characters!")

    empty_string = ""
    for char in text:
        # for index, value in morse_code.items():
        #     if char == index:
        #         empty_string += value
        empty_string += morse_code.get(char)

    print(empty_string)


def main():
    text_input = str(input("Enter a few words:")).upper()
    morse_code_fun(text_input)

if __name__ == '__main__':
    main()
