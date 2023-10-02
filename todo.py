todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def list_tasks():
    print("Tasks in the to-do list:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

def remove_task(index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index. No task removed.")

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter task description: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
