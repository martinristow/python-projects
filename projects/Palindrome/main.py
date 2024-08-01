# TODO: Create a program that can check text to see if it is a Palindrome
def check_palindrome(text):
    reverse_text = ""
    for char in range(len(text)-1, -1, -1):
        reverse_text += text[char]

    if text == reverse_text:
        print(f"The word {text} is a Palindrome!")
    else:
        print(f"The word {text} is not a Palindrome")


text = input("Enter a text: ").lower()

check_palindrome(text)