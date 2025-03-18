import time

def make_unique_task(tasks, task_name):
    lower_tasks = [task.lower() for task in tasks]
    if task_name.lower() not in lower_tasks:
        return task_name

    count = 1
    while f"{task_name} ({count})".lower() in lower_tasks:
        count += 1
    return f"{task_name} ({count})"

def get_yes_no_input(yes_no_question):
    while True:
        response = input(yes_no_question).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_valid_task_input(task_prompt, tasks=None, allow_existing=False):
    while True:
        task_name = input(task_prompt).strip()
        if task_name == "":
            print("Error: Task cannot be empty. Please enter a task.")
            continue
        if tasks is not None and not allow_existing:
            if task_name.lower() in (task.lower() for task in tasks):
                print(f"Task '{task_name}' already exists. Please enter a different task.")
                continue
        return task_name

def add_task(tasks):
    task_name = get_valid_task_input("Enter task you want to add = ", tasks)
    if get_yes_no_input(f"Do you want to add the task '{task_name}'? (yes/no): "):
        tasks.append(task_name)
        print(f"Task '{task_name}' has been successfully added.")
    else:
        print("Task addition cancelled.")

def update_task(tasks):
    updated_val = get_valid_task_input("Enter the task name you want to update = ", tasks, allow_existing=True)
    if updated_val.lower() not in (task.lower() for task in tasks):
        print("Task not found. Please enter an existing task name.")
        return
    
    new_task = get_valid_task_input("Enter new task = ", tasks)
    if get_yes_no_input(f"Do you want to update '{updated_val}' to '{new_task}'? (yes/no): "):
        ind = next(i for i, task in enumerate(tasks) if task.lower() == updated_val.lower())
        tasks[ind] = new_task
        print(f"Updated task '{updated_val}' to '{new_task}'.")
    else:
        print("Task update cancelled.")

def delete_task(tasks):
    del_val = get_valid_task_input("Which task you want to delete = ", tasks, allow_existing=True)
    if del_val.lower() not in (task.lower() for task in tasks):
        print("Task not found. Please enter an existing task name.")
        return
    
    if get_yes_no_input(f"Are you sure you want to delete the task '{del_val}'? (yes/no): "):
        ind = next(i for i, task in enumerate(tasks) if task.lower() == del_val.lower())
        del tasks[ind]
        print(f"Task '{del_val}' has been deleted.")
    else:
        print("Task deletion cancelled.")

def task():
    tasks = []
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    total_task = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_task + 1):
        task_name = get_valid_task_input(f"Enter task {i} = ", tasks)
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
            if operation == 1:
                add_task(tasks)
            elif operation == 2:
                update_task(tasks)
            elif operation == 3:
                delete_task(tasks)
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            elif operation == 5:
                print("Closing the program....\n")
                time.sleep(1)
                print("The program has been closed successfully!!!!!!!!!")
                break
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()jdhfksjks