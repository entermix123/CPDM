from django.core.exceptions import ValidationError


def validate_employee_first_name(first_name):
    is_valid = any(ch.isalnum() or ch == '_' for ch in first_name)

    if not is_valid:
        raise ValidationError("First Name must contain only letters, digits, and underscores!")


def validate_employee_last_name(last_name):
    is_valid = any(ch.isalnum() or ch == '_' for ch in last_name)

    if not is_valid:
        raise ValidationError("Last Name must contain only letters, digits, and underscores!")
