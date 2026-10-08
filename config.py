import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

STUDENT_FILE = os.path.join(DATA_DIR, "students.json")
FEE_FILE = os.path.join(DATA_DIR, "fees.json")
PAYMENT_FILE = os.path.join(DATA_DIR, "payments.json")

FEE_TYPES = [
    "Tuition",
    "Library",
    "Laboratory",
    "Sports",
    "Transport",
    "Examination",
    "Other"
]

PAYMENT_MODES = [
    "Cash",
    "UPI",
    "Card",
    "Bank Transfer"
]
