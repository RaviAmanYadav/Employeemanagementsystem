def generate_id(data):
    if not data:
        return 1
    return max(emp["id"] for emp in data) + 1
