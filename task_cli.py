import sys
import json
import os
from datetime import datetime

FILE_PATH = "tasks.json"

"""Reads tasks from JSON file. Creates it  if it doesn't exists."""
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

"""Writes tasks to json file"""
def save_tasks(tasks):
    with open(FILE_PATH, 'w') as f:
        json.dump(tasks, f, indent = 4)

def get_current_time():
    return datetime.now().isoformat()

"""Generates an auto-incrementing ID for new tasks"""
def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    now = get_current_time()

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id}) ")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = get_current_time()
            save_tasks(tasks)
            print(f"Task {task_id} is successsfully updated")
            return
    print(f"ERROR: Task {task_id} Not found.")

def delete_task(task_id):
    tasks = load_tasks()
    init_count = len(tasks)

    tasks = [task for task in tasks if task['id'] != task_id]

    if len(tasks) < init_count:
        save_tasks(tasks)
        print(f"Task {task_id} is successsfully Deleated")
    else:
        print(f"ERROR: Task {task_id} Not found.")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = get_current_time()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"ERROR: Task {task_id} Not found.")

def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task['status'] == status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [agrguments]")
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Missing description. Usage: task-cli add \"\"")
            else:
                add_task(sys.argv[2])

        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Missing arguments. Usage: task-cli update \"\"")
            else:
                update_task(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Missing task ID. Usage: task-cli delete ")
            else:
                delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Missing task ID. Usage: task-cli mark-in-progress ")
            else:
                mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Missing task ID. Usage: task-cli mark-done ")
            else:
                mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            if len(sys.argv) == 3:
                status = sys.argv[2]
                if status in ["todo", "in-progress", "done"]:
                    list_tasks(status)
                else:
                    print("Error: Invalid status. Use 'todo', 'in-progress', or 'done'.")
            else:
                list_tasks()

        else:
            print(f"Error: Unknown command '{command}'.")

    except ValueError:
        print(f"Error: Task ID must be a number.")

if __name__ == "__main__":
    main()