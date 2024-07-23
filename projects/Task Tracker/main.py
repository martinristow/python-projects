import functions

exit_for_app = False

while not exit_for_app:
    print("If you want to add a new task, enter a '1':")
    print("If you want to remove a task, enter '2':")
    print("If you want to update status to a task, enter '3':")
    print("If you want to view all task, enter '4':")
    task = int(input())
    if task == 1:
        functions.add_task()
    elif task == 2:
        functions.remove_task()
    elif task == 3:
        functions.update_status_task()
    elif task == 4:
        functions.print_all_task()
    else:
        exit_for_app = True