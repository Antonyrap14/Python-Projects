students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 62},
    {"name": "Clara", "grade": 90},
    {"name": "David", "grade": 58},
    {"name": "Eva", "grade": 76},
]

def over_70(students):
    student_over_70 = [
        student for student in students if student["grade"] >= 70
    ]
    print(student_over_70)

over_70(students)