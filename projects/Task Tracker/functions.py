
tasks = []
def add_task():
    name = input("What is the name of task : ").title()
    priority = input("What is the priority of task (lower, mid, highest) ? :").title()
    status = "Unfinished"

    task = {"Name": name, "Priority": priority,"Status":status}
    tasks.append(task)
    # print(tasks)


def remove_task():
    name = input("Type the name of the task you want to delete:\n")
    for task in tasks:
        if task["Name"] == name:
            tasks.remove(task)
            print("Task is remove successfully")
        else:
            print("Task is not find")


def update_status_task():
    print(f"List od all tasks: {tasks} ")
    name = input("Enter a name of task: ")
    for task in tasks:
        if task["Name"] == name:
            status = input("What is the status of this task : (Finished / Unfinished) ?")
            task["Status"] = status
            print(f"Successfully updated a status of {task["Name"]}")


def print_all_task():
    finished_task = []
    unfinished_task = []
    print("If you want to view all task, enter '1'")
    print("If you want to view filtered task based on status, enter '2'")
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
        print("You enter a wrong number! Only '1' or '2'.")

#   6) Function to sort tasks:
# Create a function that sorts tasks by priority and displays the sorted tasks.

def sort_task():
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