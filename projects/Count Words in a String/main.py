# TODO: Create a program that can count words and characters in a String.
def count_words_and_char(text):
    counter_words = 0
    counter_char = 0
    split_text = text.split()

    for char in text:
        counter_char += 1

    for word in split_text:
        counter_words += 1

    print(f"You have: {counter_words} words in your text!")
    print(f"You have: {counter_char} characters in your text!")

    # Other way for this short project :)
    print("")
    better_counter_words = len(text.split())
    better_counter_char = len(text)

    print(f"In this short code you have: {better_counter_words} words!")
    print(f"In this short code you have: {better_counter_char} characters")

text = input("Enter a large text: ")
count_words_and_char(text = text)










