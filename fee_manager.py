from config import FEE_FILE, STUDENT_FILE, FEE_TYPES
from storage import load_data, save_data
from utils import generate_id, find_by_id


def create_fee_structure():
    students = load_data(STUDENT_FILE)
    fees = load_data(FEE_FILE)

    student_id = input("Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\nFee Types:")

    for index, fee_type in enumerate(FEE_TYPES, 1):
        print(f"{index}. {fee_type}")

    try:
        choice = int(input("Select Fee Type: "))

        if not 1 <= choice <= len(FEE_TYPES):
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid input.")
        return

    amount = input("Fee Amount: ").strip()

    try:
        amount = float(amount)

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    fee = {
        "id": generate_id("FEE"),
        "student_id": student_id,
        "fee_type": FEE_TYPES[choice - 1],
        "amount": amount
    }

    fees.append(fee)

    save_data(FEE_FILE, fees)

    print("Fee structure added successfully!")
    print("Fee ID:", fee["id"])


def view_fee_structures():
    fees = load_data(FEE_FILE)

    if not fees:
        print("No fee structures found.")
        return

    students = load_data(STUDENT_FILE)

    print("\n========== FEE STRUCTURES ==========")

    for fee in fees:
        student = find_by_id(
            students,
            fee["student_id"]
        )

        student_name = (
            student["name"]
            if student
            else "Unknown"
        )

        print("-" * 45)
        print("Fee ID:", fee["id"])
        print("Student:", student_name)
        print("Student ID:", fee["student_id"])
        print("Fee Type:", fee["fee_type"])
        print("Amount: ₹", fee["amount"])


def calculate_student_fee(student_id):
    fees = load_data(FEE_FILE)

    return sum(
        fee["amount"]
        for fee in fees
        if fee["student_id"] == student_id
    )
