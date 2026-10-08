from config import STUDENT_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_student():
    students = load_data(STUDENT_FILE)

    name = input("Student Name: ").strip()
    class_name = input("Class: ").strip()
    division = input("Division: ").strip()
    roll_number = input("Roll Number: ").strip()
    parent_name = input("Parent Name: ").strip()
    phone = input("Parent Phone: ").strip()

    if not all([
        name,
        class_name,
        division,
        roll_number,
        parent_name,
        phone
    ]):
        print("All fields are required.")
        return

    student = {
        "id": generate_id("STU"),
        "name": name,
        "class": class_name,
        "division": division,
        "roll_number": roll_number,
        "parent_name": parent_name,
        "phone": phone
    }

    students.append(student)
    save_data(STUDENT_FILE, students)

    print("\nStudent added successfully!")
    print("Student ID:", student["id"])


def view_students():
    students = load_data(STUDENT_FILE)

    if not students:
        print("No students found.")
        return

    print("\n========== STUDENTS ==========")

    for student in students:
        print("-" * 45)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Class:", student["class"])
        print("Division:", student["division"])
        print("Roll Number:", student["roll_number"])
        print("Parent:", student["parent_name"])
        print("Phone:", student["phone"])


def search_student():
    students = load_data(STUDENT_FILE)

    keyword = input(
        "Enter Student ID, Name or Roll Number: "
    ).strip().lower()

    results = []

    for student in students:
        if (
            keyword in student["id"].lower()
            or keyword in student["name"].lower()
            or keyword in student["roll_number"].lower()
        ):
            results.append(student)

    if not results:
        print("Student not found.")
        return

    for student in results:
        print("-" * 40)
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Class:", student["class"])
        print("Division:", student["division"])
        print("Roll Number:", student["roll_number"])


def update_student():
    students = load_data(STUDENT_FILE)

    student_id = input("Enter Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\nPress Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    phone = input(f"Phone [{student['phone']}]: ").strip()
    parent = input(
        f"Parent Name [{student['parent_name']}]: "
    ).strip()

    if name:
        student["name"] = name

    if phone:
        student["phone"] = phone

    if parent:
        student["parent_name"] = parent

    save_data(STUDENT_FILE, students)

    print("Student updated successfully!")


def delete_student():
    students = load_data(STUDENT_FILE)

    student_id = input("Enter Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    students.remove(student)

    save_data(STUDENT_FILE, students)

    print("Student deleted successfully!")
