# Import functions from task_manager.task_utils package
from task_manager.task_utils import *

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            try: 
                add_task(title, description, due_date)
            except ValueError as e:
                print(e)

        elif choice == "2":
            index = int(input("Enter task index (0 to exit): "))
            if index != 0:
                mark_task_as_complete(index - 1)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(progress)

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
