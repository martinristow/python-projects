import pandas

data_set = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data_set.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
