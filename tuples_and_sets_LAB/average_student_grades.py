# def input_to_list(count):
#     lines = []
#     for _ in range(count):
#         lines.append(input())
#     return lines
#
#
# n = int(input())
#
# students = input_to_list(n)


n = int(input())
students = []

for _ in range(n):
    students.append(input())


def avg(values):
    return sum(values)/len(values)


students_grades = {}

for line in students:
    student, grade = line.split()

    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student, grades in students_grades.items():
    # grades_str = " ".join(map(lambda grade: f'{grade:.2f}', grades))
    grades_str = " ".join(f'{grade:.2f}' for grade in grades)
    avg_grade = avg(grades)
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")