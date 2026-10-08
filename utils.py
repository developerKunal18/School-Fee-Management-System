import uuid
from datetime import datetime


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(records, record_id, key="id"):
    return next(
        (
            record
            for record in records
            if record.get(key) == record_id
        ),
        None
    )


def format_currency(amount):
    return f"₹{amount:.2f}"


def get_number(message):
    try:
        value = float(input(message))

        if value < 0:
            print("Amount cannot be negative.")
            return None

        return value

    except ValueError:
        print("Enter a valid number.")
        return None
