def validate_employee_first_name(first_name):
    is_valid = any(x.isalnum() or x == '_' for x in first_name)

    if not is_valid:
        raise ValueError("First Name must contain only letters, numbers and underscores.")


def validate_employee_last_name(last_name):
    is_valid = any(x.isalnum() or x == '_' for x in last_name)

    if not is_valid:
        raise ValueError("Last Name must contain only letters, numbers and underscores.")
