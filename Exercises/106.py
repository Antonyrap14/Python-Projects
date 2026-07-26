def calculate_grade(student_name, score):
    if score >= 90:
        return "{0} student has received ’A’".format(
            student_name
        )
    elif score >= 80:
        return "{0} student has received ’B’".format(
            student_name
        )
    elif score >= 70:
        return "{0} student has received ’C’".format(
            student_name
        )
    elif score >= 60:
        return "{0} student has received ’D’".format(
            student_name
        )
    else:
        return "{0} student has received ’F’".format(
            student_name
        )

student_name = input("Enter the student’s name: ")
score = int(input("Enter the student’s score: "))
print(calculate_grade(student_name, score))


