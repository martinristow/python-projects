import functions

def display_menu():
    """
    Displays the main menu with options for task management.
    """
    print("\n--- Task Management System ---\n")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Update task status")
    print("4. View all tasks")
    print("5. Sort tasks by priority")
    print("0. Exit")
    print("--------------------------------")


def get_user_choice():
    """
    Prompts the user to enter a menu choice and returns the chosen option.

    Returns:
    int: The user's menu choice.
    """
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1


def main():
    """
    Main function to run the task management system.
    """
    exit_for_app = False

    while not exit_for_app:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            functions.add_task()
        elif choice == 2:
            functions.remove_task()
        elif choice == 3:
            functions.update_status_task()
        elif choice == 4:
            functions.print_all_task()
        elif choice == 5:
            functions.sort_task()
        elif choice == 0:
            exit_for_app = True
            print("Exiting the Task Management System. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
