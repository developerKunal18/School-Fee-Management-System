from student_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from fee_manager import (
    create_fee_structure,
    view_fee_structures
)

from payment_manager import (
    collect_fee,
    view_payments,
    student_fee_status
)

from report_manager import (
    fee_collection_report,
    class_wise_report,
    pending_fee_report
)


def main():

    while True:

        print("\n" + "=" * 50)
        print("       SCHOOL FEE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("\nSTUDENT MANAGEMENT")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")

        print("\nFEE MANAGEMENT")
        print("6. Create Fee Structure")
        print("7. View Fee Structures")

        print("\nPAYMENT MANAGEMENT")
        print("8. Collect Fee")
        print("9. View Payment History")
        print("10. Check Student Fee Status")

        print("\nREPORTS")
        print("11. Fee Collection Report")
        print("12. Class Wise Report")
        print("13. Pending Fee Report")

        print("\n0. Exit")

        choice = input("\nEnter your choice: ").strip()

        actions = {
            "1": add_student,
            "2": view_students,
            "3": search_student,
            "4": update_student,
            "5": delete_student,
            "6": create_fee_structure,
            "7": view_fee_structures,
            "8": collect_fee,
            "9": view_payments,
            "10": student_fee_status,
            "11": fee_collection_report,
            "12": class_wise_report,
            "13": pending_fee_report
        }

        if choice == "0":
            print("\nThank you for using School Fee Management System!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
