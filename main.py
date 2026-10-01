#Add Student 
students = [
    {
        "name": "Aman",
        "marks": {
            "Physics": 78,
            "Chemistry": 82,
            "Maths": 91
        }
    },
    {
        "name": "Riya",
        "marks": {
            "Physics": 95,
            "Chemistry": 79,
            "Maths": 88
        }
    },
    {
        "name": "Kabir",
        "marks": {
            "Physics": 84,
            "Chemistry": 96,
            "Maths": 90
        }
    }
]
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
# Class Topper
def class_topper():
    if not students:
        print("No Students Record Found!")
        return 
    topper=students[0]
    Highest_percentage=calculate_percentage(topper)
    for student in students[1:]:
        percentage=calculate_percentage(student)
        if percentage>Highest_percentage:
            topper=student 
            Highest_percentage=percentage
    print("\nClass Topper")
    print("Name:", topper["name"])
    print("Percentage:", round(Highest_percentage, 2))
    print("Grade:", calculate_grade(Highest_percentage))

# Subject topper
def subject_topper():
    if not students:
        print("No Students Record Found!")
        return
    subject= input("Enter subjcet name: ").strip().title()
    topper= None 
    highest_marks=-1
    for student in students:
        marks=student['marks'].get(subject)
        if marks is not None and  marks>highest_marks:
            topper=student
            highest_marks=marks 
    if topper is None:
        print("Subject Not Found!")
    else:
        print("\nSubject Topper")
        print("Subject:", subject)
        print("Name:", topper["name"])
        print("Marks:", highest_marks)
# Class Average 
def class_average():
    if not students:
        print("No Students Record Found!")
    percentages=[]
    for student in students:
        percentage=calculate_percentage(student)
        percentages.append(percentage)
    average=sum(percentages)/len(percentages)
    print("\nClass Average:", round(average, 2))

# Student Ranking 
def rank_students():
    if not students:
        print("No Student Record Found!")
        return 
    ranked_students=sorted(students,
                           key=calculate_percentage,
                            reverse=True )
    print("\nStudent Ranking")

    rank=1

    for student in ranked_students:
        percentage=calculate_percentage(student)
        print(
            rank,
            student["name"],
            "-",
            round(percentage, 2),
            "%"
        )

        rank+=1

# Update Student Marks
def update_student_marks():
    if not students:
        print("No Students Record Found!")
        return
    name=input("\n Enter student name: ").strip().lower()
    for student in students:
        if student["name"].lower()==name:
            print("\n Current Marks:")
            for subject, mark in student['marks'].items():
                print(subject,":",mark)
            subject=input("\n Enter subject to update:").strip().title()

            if subject not in student["marks"]:
                print("Subject not found!")
                return
            new_mark=input("Enter new mark:").strip()
            if not new_mark.isdigit():
                print("Marks must be a number!")
                return
            
            new_mark=int(new_mark)

            if new_mark < 0 or new_mark > 100:
                print("Marks must be between 0 and 100.")
                return

            student["marks"][subject] = new_mark

            print("\nMarks updated successfully.")
            print(subject, ":", new_mark)

            return

    print("Student not found.")






# Menu 
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYZER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Percentage")
        print("5. Show Class Topper")
        print("6. Show Subject Topper")
        print("7. Show Class Average")
        print("8. Show Student Ranking")
        print("9. Update Student Marks")
        print("10. Exit")

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
        elif choice=="5":
             class_topper()
        elif choice=="6":
            subject_topper()
        elif choice=="7":
            class_average()

        elif choice == "8":
            rank_students()
        elif choice=="9":
            update_student_marks()

        elif choice == "10":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()

     
    

       
