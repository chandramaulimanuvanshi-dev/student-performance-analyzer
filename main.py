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

# Calculate Percentage 
def calculate_percentage(student):
     marks=student['marks'].values()
     return sum(marks)/len(marks)

# Menu 
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Show Percentage")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            if not students:
                print("No students found.")
            else:
                for student in students:
                    percentage = calculate_percentage(student)
                    print(student["name"], ":", percentage)

        elif choice == "4":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()
     
    

       
