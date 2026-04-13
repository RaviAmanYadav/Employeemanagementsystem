def generate_id(data):
    if not data:
        return 1
    return max(emp["emp_id"] for emp in data) + 1
