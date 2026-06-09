

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        file = open(TASKS_FILE, "r")
        for line in file:
            line = line.strip()
            if line:
                tasks.append(line)
        file.close()
    except FileNotFoundError:
        pass  # No file yet, start with empty list
    return tasks

def save_tasks(tasks):
    file = open(TASKS_FILE, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])

def add_task(tasks):
    title = input("Enter task name: ")
    print("Priority: 1. High  2. Medium  3. Low")
    choice = input("Choose priority (1/2/3): ")

    if choice == "1":
        priority = "[High]"
    elif choice == "3":
        priority = "[Low]"
    else:
        priority = "[Medium]"

    task = priority + " " + title + " - Pending"
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Invalid number.")
            return
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print("Deleted: " + removed)
    except ValueError:
        print("Please enter a valid number.")

def mark_complete(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        if num < 1 or num > len(tasks):
            print("Invalid number.")
            return
        task = tasks[num - 1]
        if "Pending" in task:
            tasks[num - 1] = task.replace("Pending", "Completed")
            print("Task marked as Completed!")
        else:
            tasks[num - 1] = task.replace("Completed", "Pending")
            print("Task marked as Pending!")
        save_tasks(tasks)
    except ValueError:
        print("Please enter a valid number.")

def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()
    print("\n--- Search Results ---")
    found = False
    for i in range(len(tasks)):
        if keyword in tasks[i].lower():
            print(str(i + 1) + ". " + tasks[i])
            found = True
    if not found:
        print("No tasks found with that keyword.")

def show_stats(tasks):
    total = len(tasks)
    completed = 0
    pending = 0
    for task in tasks:
        if "Completed" in task:
            completed += 1
        else:
            pending += 1
    print("\n--- Task Statistics ---")
    print("Total tasks  :", total)
    print("Completed    :", completed)
    print("Pending      :", pending)

# Main program
print("=== To-Do List Application ===")

tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View all tasks")
    print("3. Delete task")
    print("4. Mark task complete / pending")
    print("5. Search task")
    print("6. Show statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        mark_complete(tasks)
    elif choice == "5":
        search_task(tasks)
    elif choice == "6":
        show_stats(tasks)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")