alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number_of_elements_in_alphabet = len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_len = len(text)
new_text = ""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs. DONE


#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. DONE
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

def encrypt(plain_text, shift_amount):
    new_text = ""
    for char in plain_text:
        position = alphabet.index(char) + shift_amount
        new_text += alphabet[position]
    print(f"The encoded text is {new_text}")

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


    # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(decrypt_text,shift_text):
    decrypt_new_text = ""
    for char in decrypt_text:
        position = alphabet.index(char) - shift_text
        decrypt_new_text += alphabet[position]
    print(f"The encoded text is {decrypt_new_text}")
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to mail_test_project the code to encrypt *AND* decrypt a message.
if direction == "decode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "encode":
    decrypt(decrypt_text=text, shift_text=shift)



    # print("You entered an error selection! Only 'encode' or 'decode' !")

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to mail_test_project the code and encrypt a message.

