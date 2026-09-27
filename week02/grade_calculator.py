grade = 0
students = 0

while True:
    name = input("Enter student name (or q to quit): ")
    if name == "q":
        break

    grade_input = input("Enter grade: ")
    grade = float(grade_input)

    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a number between 0 and 100.")
        continue

    students += 1

    if grade <= 59:
        print("F")
    elif grade <= 69:
        print("D")
    elif grade <= 79:
        print("C")
    elif grade <= 89:
        print("B")
    else:
        print("A")

print(f"total students graded: {students}")
