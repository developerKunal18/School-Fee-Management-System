from config import (
    STUDENT_FILE,
    FEE_FILE,
    PAYMENT_FILE
)

from storage import load_data, save_data
from utils import find_by_id


def fee_collection_report():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)
    payments = load_data(PAYMENT_FILE)

    total_fee = sum(
        fee["amount"]
        for fee in fees
    )

    total_collected = sum(
        payment["amount"]
        for payment in payments
    )

    total_pending = total_fee - total_collected

    print("\n========== FEE COLLECTION REPORT ==========")

    print("Total Students:", len(students))
    print("Total Assigned Fee: ₹", total_fee)
    print("Total Collected: ₹", total_collected)
    print("Total Pending: ₹", total_pending)

    print("=" * 45)


def class_wise_report():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)
    payments = load_data(PAYMENT_FILE)

    classes = sorted(
        set(student["class"] for student in students)
    )

    if not classes:
        print("No class data available.")
        return

    print("\n========== CLASS WISE REPORT ==========")

    for class_name in classes:

        class_students = [
            student
            for student in students
            if student["class"] == class_name
        ]

        student_ids = {
            student["id"]
            for student in class_students
        }

        total_fee = sum(
            fee["amount"]
            for fee in fees
            if fee["student_id"] in student_ids
        )

        total_paid = sum(
            payment["amount"]
            for payment in payments
            if payment["student_id"] in student_ids
        )

        print("-" * 40)
        print("Class:", class_name)
        print("Students:", len(class_students))
        print("Total Fee: ₹", total_fee)
        print("Collected: ₹", total_paid)
        print("Pending: ₹", total_fee - total_paid)


def pending_fee_report():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)
    payments = load_data(PAYMENT_FILE)

    print("\n========== PENDING FEE REPORT ==========")

    found = False

    for student in students:

        student_id = student["id"]

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

        if pending > 0:
            found = True

            print("-" * 45)
            print("Student:", student["name"])
            print("Class:", student["class"])
            print("Total Fee: ₹", total_fee)
            print("Paid: ₹", paid)
            print("Pending: ₹", pending)

    if not found:
        print("No pending fees.")
