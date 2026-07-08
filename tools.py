import json
import os
from langchain.tools import tool

# long term memory ----> simple file-based storage for tasks
TASKS_FILE = "data/tasks.json"
COMPLETED_TASKS_FILE = "data/completed_tasks.json"

# Helper function (read tasks from file)
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Helper function (save tasks to file)
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# tool 1: Add Task 
@tool
def add_task(task_description):
    """Adds a new task to the task list. Input should be the task description."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "task": task_description,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return f"Task added successfully: '{task_description}' (ID: {new_task['id']})"


#  TOOL 2: View Tasks 
@tool
def view_tasks(query):
    """Shows all current tasks with their status. Use this when user asks to see/list their tasks."""
    tasks = load_tasks()
    
    if not tasks:
        return "No tasks found. Your task list is empty."
    
    result = "Here are your tasks:\n"
    for t in tasks:
        status = "Done" if t["completed"] else "Pending"
        result += f"ID {t['id']}: {t['task']} [{status}]\n"
    
    return result

# TOOL 3: Complete Task
def load_completed_tasks():
    if not os.path.exists(COMPLETED_TASKS_FILE):
        return []
    try:
        with open(COMPLETED_TASKS_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        return []

def save_completed_tasks(tasks):
    with open(COMPLETED_TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

 
@tool
def complete_task(task_id):
    """Marks a task as completed and moves it to completed tasks history. Input should be the task ID number."""
    tasks = load_tasks()
    
    try:
        task_id = int(task_id)
    except ValueError:
        return "Please provide a valid task ID number."
    
    for t in tasks:
        if t["id"] == task_id:
            # Remove from Active list
            tasks.remove(t)
            save_tasks(tasks)
            
            # Add to Completed list
            t["completed"] = True
            completed = load_completed_tasks()
            completed.append(t)
            save_completed_tasks(completed)
            
            return f"Task ID {task_id} completed and moved to history: '{t['task']}'"
    
    return f"Task ID {task_id} not found."


# TOOL 4: View Completed Tasks 
@tool
def view_completed_tasks(query):
    """Shows all completed tasks history. Use this when user asks to see completed/done/finished tasks."""
    completed = load_completed_tasks()
    
    if not completed:
        return "No completed tasks yet."
    
    result = "Here are your completed tasks:\n"
    for t in completed:
        result += f"ID {t['id']}: {t['task']} Done\n"
    
    return result