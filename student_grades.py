# Initialize the dictionary
student_grades = {}

while True:
    print("\nStudent Grades Menu")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"{name} does not exist.")

    elif choice == '3':
        if not student_grades:
            print("No student data available.")
        else:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
