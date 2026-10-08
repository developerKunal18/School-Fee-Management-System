# School Fee Management System

A Python-based School Fee Management System for managing
students, fee structures, payments, receipts, and reports.

## Features

- Add students
- View students
- Search students
- Update student details
- Delete students
- Create fee structures
- View fee structures
- Collect fees
- Generate receipt numbers
- View payment history
- Check student fee status
- Generate fee collection reports
- Generate class-wise reports
- Generate pending fee reports
- JSON data storage

## Technologies

- Python
- JSON
- Datetime
- UUID
- OS

## Folder Structure

```text
school-fee-management/
│
├── main.py
├── config.py
├── storage.py
├── utils.py
├── student_manager.py
├── fee_manager.py
├── payment_manager.py
├── report_manager.py
│
├── data/
│   ├── students.json
│   ├── fees.json
│   └── payments.json
│
├── .gitignore
└── README.md
