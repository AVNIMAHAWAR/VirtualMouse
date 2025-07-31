student_grades = {}  #empty dict user will add content as stud:grade

def add_Stud(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")   #f se {name} ki jagah avni and {grade} ki jagah O print hoga
                                                # varna it prints Added {name} with grade {grade}
def update_Stud(name,grade):
    if(name in student_grades):
        student_grades[name] = grade
        print(f"{name}'s gardes are updated as {grade}")

    else:
        print(f"{name} not found!")

def del_Stud(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name}'s details successfully deleted")

    else:
        print(f"{name} not found")

def view_Details():
    if student_grades:
        for name,grade in student_grades.items():  #item() dictionary ke saare ele display kara dega
            print(f"{name}:{grade}")    

    else:
        print(f"not found")

def view():
    print(student_grades)
    
def main():
    while True:
        print("-----STUDENT MANAGEMENT SYS-----")
        print("1.Add a student\n2.Update Details\n3.Delete details of a student\n4.View details\n5.Exit")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter name:")
            grade = input("Enter grade:")
            add_Stud(name,grade)

        elif choice == 2:
            name = input("Enter name:")
            grade = input("Enter grade:")
            update_Stud(name,grade)

        elif choice == 3:
            name = input("Enter name:")
            del_Stud(name)

        elif choice == 4:       #isse avni:A
            view_Details()      #     ayush:A+    aese proper print hoga

        # elif choice == 5:      isse {'avni':'A', 'ayush':'A+'} aesa print hoga
        #     view()

        elif choice == 5:
            print("Closing the program")
            break

        else:
            print("Invalid choice")

main()