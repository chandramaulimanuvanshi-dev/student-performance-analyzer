#Add Student 
students=[]
def add_student():
    name=input("Enter student name: ")
    marks_input=input("Enter Physics, Chemistry  and Maths Marks: ")
    marks=list(map(int,marks_input.split()))
    subjects=["Physics","Chemistry","Maths"]
    student_marks=dict(zip(subjects,marks))
    student={
        "name":name,
        "marks":student_marks
    }
    students.append(student)
    print("Student Added Successfully")

# View Students 
def view_students():
   if not students:
       print("No Students Record Found!") 
       return 
   for student in students:
           print(student)
# Search Student 
def search_student():
    name=input("Eenter student name: ").strip().lower()

    for student in students:
        if student['name'].lower()==name:
            print('\n Student Found:')
            print('Name:',student['name'])
            print('Marks',student['marks'])
            return 
    print('Student Not Found.')

# Calculate Percentage 
def calculate_percentage(student):
    marks = student["marks"].values()
    return sum(marks) / len(marks)
# Calculate grade

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Menu 
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Percentage")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()
        elif choice=='3':
            search_student()

        elif choice == "4":
            if not students:
                print("No students found.")
            else:
                for student in students:
                    percentage = calculate_percentage(student)
                    grade = calculate_grade(percentage)

                    print(
                            student["name"],
                            "- Percentage:",
                            round(percentage, 2),
                            "- Grade:",
                            grade
                                 )

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()

     
    

       
