import functions

def main():
    add = True
    while add:
        functions.display_menu()
        choice = input("\nPlease select an option (0-10): ")
        print("\n")
        if choice.isdigit():
            digit = int(choice)
            if digit == 1:
                functions.add_new_product()
            elif digit == 2:
                functions.show_inventory()
            elif digit == 3:
                functions.update_quantity()
            elif digit == 4:
                functions.update_price()
            elif digit == 5:
                functions.remove_product()
            elif digit == 6:
                functions.sell_product()
            elif digit == 7:
                functions.warning_message()
            elif digit == 8:
                functions.show_report()
            elif digit == 9:
                functions.add_promotions_or_discounts()
            elif digit == 10:
                functions.show_promotions_or_discounts()
            elif digit == 0:
                print("Exiting the program. Goodbye!")
                add = False
            else:
                print("Invalid option. Please select a number between 0 and 10.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
