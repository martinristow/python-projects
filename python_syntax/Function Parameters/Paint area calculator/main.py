import math

def paint_calc(height,width,cover):
    # print(height,width,cover)
    number_of_cans = (height * width) / cover
    rounded_result = math.ceil(number_of_cans)
    print(f"You'll need {rounded_result} cans of paint.")

test_h = int(input("Height of wall (m):\n"))
test_w = int(input("Width of wall (m):\n"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
