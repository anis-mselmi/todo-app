from tasks import add_task, list_tasks, mark_done

def menu():
    while True:
        print("\n=== TO-DO LIST APP ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                num = int(input("Enter task number: ")) - 1
                mark_done(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
