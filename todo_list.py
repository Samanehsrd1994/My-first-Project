tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):  # Fixed typo here
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty!")

# Example usage
add_task("Finish GitHub project")
view_tasks()