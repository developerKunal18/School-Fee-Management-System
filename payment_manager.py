from config import (
    PAYMENT_FILE,
    STUDENT_FILE,
    FEE_FILE,
    PAYMENT_MODES
)

from storage import load_data, save_data
from utils import (
    generate_id,
    current_datetime,
    find_by_id
)


def calculate_paid(student_id):
    payments = load_data(PAYMENT_FILE)

    return sum(
        payment["amount"]
        for payment in payments
        if payment["student_id"] == student_id
    )


def collect_fee():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)
    payments = load_data(PAYMENT_FILE)

    student_id = input("Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    total_fee = sum(
        fee["amount"]
        for fee in fees
        if fee["student_id"] == student_id
    )

    paid = calculate_paid(student_id)
    pending = total_fee - paid

    print("\nStudent:", student["name"])
    print("Total Fee: ₹", total_fee)
    print("Paid: ₹", paid)
    print("Pending: ₹", pending)

    if pending <= 0:
        print("No pending fee.")
        return

    try:
        amount = float(
            input("Payment Amount: ")
        )

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > pending:
            print("Payment cannot exceed pending fee.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    print("\nPayment Modes:")

    for index, mode in enumerate(PAYMENT_MODES, 1):
        print(f"{index}. {mode}")

    try:
        choice = int(input("Select Payment Mode: "))

        if not 1 <= choice <= len(PAYMENT_MODES):
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid choice.")
        return

    payment = {
        "receipt_no": generate_id("REC"),
        "student_id": student_id,
        "amount": amount,
        "payment_mode": PAYMENT_MODES[choice - 1],
        "date": current_datetime()
    }

    payments.append(payment)

    save_data(PAYMENT_FILE, payments)

    print("\nPayment successful!")
    print("Receipt Number:", payment["receipt_no"])
    print("Amount Paid: ₹", amount)


def view_payments():
    payments = load_data(PAYMENT_FILE)
    students = load_data(STUDENT_FILE)

    if not payments:
        print("No payments found.")
        return

    print("\n========== PAYMENT HISTORY ==========")

    for payment in payments:
        student = find_by_id(
            students,
            payment["student_id"]
        )

        name = student["name"] if student else "Unknown"

        print("-" * 50)
        print("Receipt:", payment["receipt_no"])
        print("Student:", name)
        print("Amount: ₹", payment["amount"])
        print("Mode:", payment["payment_mode"])
        print("Date:", payment["date"])


def student_fee_status():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)
    payments = load_data(PAYMENT_FILE)

    student_id = input("Enter Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    total_fee = sum(
        fee["amount"]
        for fee in fees
        if fee["student_id"] == student_id
    )

    paid = sum(
        payment["amount"]
        for payment in payments
        if payment["student_id"] == student_id
    )

    pending = total_fee - paid

    print("\n========== FEE STATUS ==========")
    print("Student:", student["name"])
    print("Class:", student["class"])
    print("Total Fee: ₹", total_fee)
    print("Paid: ₹", paid)
    print("Pending: ₹", pending)

    if pending <= 0:
        print("Status: PAID")
    else:
        print("Status: PENDING")
