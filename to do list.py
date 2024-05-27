def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def mark_completed(tasks, task_number):
    if task_number <= len(tasks):
        tasks[task_number - 1] += " - Completed"
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_number):
    if task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            mark_completed(tasks, task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()