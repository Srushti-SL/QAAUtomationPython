
from datetime import datetime, timedelta

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_due_date(borrow_date_str, days=14):
    borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
    due_date = borrow_date + timedelta(days=days)
    return due_date.strftime("%Y-%m-%d")


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
