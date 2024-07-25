tasks = []

def add_task():
    """
    Adds a new task to the task list with user-specified details.

    Prompts the user to enter the task's name and priority. The status is set to "Unfinished" by default.
    The task is then appended to the global `tasks` list.

    Returns:
    None
    """
    name = input("What is the name of task : ").title()
    priority = input("What is the priority of task (lower, mid, highest) ? :").title()
    status = "Unfinished"

    task = {"Name": name, "Priority": priority, "Status": status}
    tasks.append(task)
    # print(tasks)


def remove_task():
    """
    Removes a task from the task list based on the task's name.

    Prompts the user to enter the name of the task to delete. If a matching task is found, it is removed
    from the global `tasks` list. If the task is not found, an error message is printed.

    Returns:
    None
    """
    name = input("Type the name of the task you want to delete:\n")
    for task in tasks:
        if task["Name"] == name:
            tasks.remove(task)
            print("Task is removed successfully")
            return
    print("Task not found")


def update_status_task():
    """
    Updates the status of an existing task.

    Displays the list of all tasks and prompts the user to enter the name of the task to update. The user 
    then provides the new status (e.g., "Finished" or "Unfinished"). The task's status is updated accordingly.

    Returns:
    None
    """
    print(f"List of all tasks: {tasks} ")
    name = input("Enter the name of the task: ")
    for task in tasks:
        if task["Name"] == name:
            status = input("What is the status of this task : (Finished / Unfinished) ?")
            task["Status"] = status
            print(f"Successfully updated the status of {task['Name']}")
            return
    print("Task not found")


def print_all_task():
    """
    Prints tasks based on the user's selection.

    Prompts the user to choose between viewing all tasks or filtering tasks by status. If the user chooses 
    to filter, it separates tasks into "Finished" and "Unfinished" categories and prints them.

    Returns:
    None
    """
    finished_task = []
    unfinished_task = []
    print("If you want to view all tasks, enter '1'")
    print("If you want to view filtered tasks based on status, enter '2'")
    number = int(input())
    if number == 1:
        print(tasks)
    elif number == 2:
        for task in tasks:
            if task["Status"] == "Finished":
                finished_task.append(task["Name"])
            else:
                unfinished_task.append(task["Name"])
        print(f"Finished tasks : {finished_task}\n")
        print(f"Unfinished tasks: {unfinished_task}\n")
    else:
        print("You entered a wrong number! Only '1' or '2'.")


def sort_task():
    """
    Sorts and prints tasks based on their priority.

    Segregates tasks into three priority levels: "Lower", "Mid", and "Highest". Each priority level is
    printed with the corresponding tasks.

    Returns:
    None
    """
    lower_task = []
    mid_task = []
    highest_task = []

    for task in tasks:
        if task["Priority"] == "Lower":
            lower_task.append(task["Name"])
        elif task["Priority"] == "Mid":
            mid_task.append(task["Name"])
        elif task["Priority"] == "Highest":
            highest_task.append(task["Name"])

    print(f"Lower priority: {lower_task}")
    print(f"Mid priority: {mid_task}")
    print(f"Highest priority: {highest_task}")
