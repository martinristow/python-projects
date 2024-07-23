
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

def print_all_task():
    print(tasks)


def update_status_task():
    print(f"List od all tasks: {tasks} ")
    name = input("Enter a name of task: ")
    for task in tasks:
        if task["Name"] == name:
            status = input("What is the status of this task : (Finished / Unfinished) ?")
            task["Status"] = status
            print(f"Successfully updated a status of {task["Name"]}")

