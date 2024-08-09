import time

print("Welcome to SPEED TYPING TEST")

timer1 = 15
timer2 = 30

text_for_timer1 = ("Hello, how are you? Today is a wonderful day to learn new things and practice our skills. "
                   "Every day is an opportunity for a new beginning and progress!")

text_for_timer2 = ("Success is not the key to happiness. Happiness is the key to success. "
                   "If you love what you are doing, you will be successful. "
                   "Always remember to stay positive and keep pushing forward no matter the obstacles.")


def timer(new_timer):
    for i in range(new_timer, 0, -1):
        time.sleep(1)
    print("Time is up")


choose = int(input("Choose a option to mail_test_project your typing speed. Type '1' for 15 seconds or type '2' for 30 seconds: "))

if choose == 1:
    print(text_for_timer1)
    timer(timer1)
    user_text = input("Enter the text: ")
    list1 = text_for_timer1.split()
    empty_list = user_text.split()
    correct_words = 0

    for i in range(min(len(list1), len(empty_list))):
        if list1[i] == empty_list[i]:
            correct_words += 1

    print("Correct words:", correct_words)

elif choose == 2:
    print(text_for_timer2)
    timer(timer2)
    user_text = input("Enter the text: ")
    list2 = text_for_timer2.split()
    empty_list = user_text.split()
    correct_words = 0

    for i in range(min(len(list2), len(empty_list))):
        if list2[i] == empty_list[i]:
            correct_words += 1

    print("Correct words:", correct_words)

else:
    print("Invalid choice. Please enter '1' or '2'.")
