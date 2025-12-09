print("    ___A SIMPLE TODO LIST____")

todo_list = []

while True:
    print('''
    1. Create task
    2. View
    3. Delete task
    4. Edit task
    5. Exit
    ''')
    try:
        choice = int(input("Input your choice: "))
    except ValueError:
        print("Please enter a number (1-5).\n")
        continue

    if choice == 1:
        task = {
            "Activity": input("Enter Activity: ").strip(),
            "Time": input("Time of Activity: ").strip()
        }
        todo_list.append(task)
        print(f"You have successfully created: {task['Activity']} at {task['Time']}\n")

    elif choice == 2:
        if not todo_list:
            print("No tasks yet.\n")
            continue
        print("These are your activities:")
        for i, t in enumerate(todo_list, start=1):
            print(f"{i}. {t['Activity']} by {t['Time']}")
        print()

    elif choice == 3:
        if not todo_list:
            print("No tasks to remove.\n")
            continue
        print("Which of the activities do you want to remove?")
        for i, t in enumerate(todo_list, start=1):
            print(f"{i}. {t['Activity']} by {t['Time']}")
        try:
            delete = int(input("Enter the number of the activity you want to remove: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        if delete < 1 or delete > len(todo_list):
            print("That number is out of range. Try again.\n")
            continue
        removed_task = todo_list.pop(delete - 1)
        print(f"Removed: {removed_task['Activity']} by {removed_task['Time']}\n")
        if not todo_list:
            print("No tasks left.\n")
        else:
            print("Updated list of activities:")
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t['Activity']} by {t['Time']}")
            print()
    elif choice == 4:
        if not todo_list:
            print("No tasks to edit.\n")
            continue
        print("Which task do you want to edit?")
        for i, t in enumerate(todo_list, start=1):
            print(f"{i}. {t['Activity']} by {t['Time']}")
        try:
            task_edit = int(input("Enter the number of the task to edit: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        if task_edit < 1 or task_edit > len(todo_list):
            print("That number is out of range. Try again.\n")
            continue
        task = todo_list[task_edit - 1]
        new_activity = input(f"New activity name (leave blank to keep '{task['Activity']}'): ").strip()
        new_time = input(f"New time (leave blank to keep '{task['Time']}'): ").strip()
        if new_activity:
            task['Activity'] = new_activity
        if new_time:
            task['Time'] = new_time
        print(f"Task {task_edit} updated.\n")
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Choose a valid option (1-5).\n")