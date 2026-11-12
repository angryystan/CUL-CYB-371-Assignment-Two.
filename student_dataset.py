
import csv
import random

random.seed(42)

departments = [
    "Computer Science",
    "Cybersecurity",
    "Software Engineering",
    "Information Technology",
    "Data Science"
]

levels = [100, 200, 300, 400]

students = []

for i in range(1, 51):
    student = {
        "Student ID": f"CUL{i:03d}",
        "Department": random.choice(departments),
        "Level": random.choice(levels),
        "Attendance Percentage": round(random.uniform(60, 100), 2),
        "Average Examination Score": round(random.uniform(40, 100), 2)
    }

    students.append(student)

with open("students_dataset.csv", "w", newline="") as file:
    columns = [
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score"
    ]

    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(students)

print("Dataset created successfully!")
