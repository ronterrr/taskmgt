from datetime import datetime

# Import validation functions
from .validation import *

# Define tasks list
tasks = []

task = {"title": "Groceries",
 "description": "Shop at Market Basket for food", 
 "due_date": "2024-06-26",
 "completed": True}

# Implement add_task function
def add_task(title, description, due_date):

    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    tasks.append({"title": title, 
                  "description": description,
                  "due_date": due_date,
                  "completed": False})
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for i in tasks:
        if i["completed"] == False:
            print(i)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    count = 0
    for i in tasks:
        if i["completed"] == True:
            count += 1
    progress = (count / len(tasks)) * 100
    print(progress)
    return progress