from datetime import datetime, date

def validate_task_title(title):
    title = str(title).strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    return title
    
def validate_task_description(description):
    description = str(description).strip()
    if not description:
        return "-"
    return description    
    
def validate_due_date(due_date):
    try: 
        parsed_date = datetime.strptime(due_date.strip(), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        raise ValueError("Invalid Date Format: Use YYYY-MM-DD.")
    
    now = date.today()

    if parsed_date < now:
        raise ValueError("Due date cannot be in the past")
    return due_date
