from datetime import datetime, date

def validate_task_title(title):
    title = str(title).strip()
    while not title:
        print("Title cannot be empty.")
        title = input("Title: ").strip()
    return title
    
def validate_task_description(description):
    description = description.strip()
    if not description:
        return "-"
    return description    
    
def validate_due_date(due_date):
    parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    now = date.today()
    while parsed_date < now:
        print("Due date cannot be in the past")
        due_date = input("Due date: ")
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    return due_date
