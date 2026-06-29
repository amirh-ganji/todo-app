from todolist import ToDoList

todo = ToDoList()
todo.load_from_csv()

def print_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete Task")
    print("4. Change task status (done/not done)")
    print("5. Save to file")
    print("6. Exit")

while True:
    print_menu()
    choice = input("Your choice: ")

    if choice == "1":
        todo.show_tasks()

    elif choice == "2":
        title = input("Task title: ")
        description = input("Description: ")
        priority = input("Priority (low, medium, high): ")
        todo.add_task(title, description, priority)

    elif choice == "3":
        index = int(input("Task number to delete: "))
        todo.remove_task(index)

    elif choice == "4":
        index = int(input("Task number to change status: "))
        todo.toggle_task_status(index)

    elif choice == "5":
        todo.save_to_csv()
        print("Tasks saved.")

    elif choice == "6":
        todo.save_to_csv()
        print("Exit the program.")
        break

    else:
        print("Invalid input. Please enter a valid number.")
