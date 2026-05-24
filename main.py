students=[]

def add_student():
    print("\n================   ADD STUDENT  ======================")
    
    try:
        roll_no=int(input("Enter your roll number:"))
        
        for student in students:
            if student["roll_no"]==roll_no:
                print("Roll Number Already Exist")
                return
        
        name=input("Enter your name:")
        
        age=int(input("Enter your Age:"))
        grade=input("Enter your Class/Grade:")
        math_marks=float(input("Enter marks obtained in MATHS:"))
        physics_marks=float(input("Enter marks obtained in PHYSICS:"))
        chemistry_marks=float(input("Enter marks obtained in CHEMISTRY:"))
        
        total=math_marks+physics_marks+chemistry_marks
        percentage=total/3
        
        student={
            "roll_no": roll_no,
            "name":name,
            "age":age,
            "grade":grade,
            "marks": {
                "Math":math_marks,
                "Physics":physics_marks,
                "Chemistry":chemistry_marks
            },
            
            "total":total,
            "percentage":percentage
        }
        students.append(student)
        print("Student Added Successfully")
        
    except ValueError:
        print("Invalid Input! Please Enter Correct Values")
 

def view_student():
    print("\n============ STUDENT DETAILS ============")
    if len(students)==0:
        print("No Student records found!")
        return
    
    print("-"*100)
    print(f"{'Roll No':<20}{'Name':<25}{'Age':<10}{'Grade':<15}{'Total':<10}{'Percentage':<10}")  
    print("-"*100)   
    
    for student in students:
        print(f"{student['roll_no']:<20}"
              f"{student['name']:<25}"
              f"{student['age']:<10}"
              f"{student['grade']:<15}"
              f"{student['total']:<10}"
              f"{student['percentage']:.2f}%")
    
    print("-"*100)  
    
def search_student():
    print("\n================== Search Student =======================")  
    
    if len(students)==0:
        print("No student records found")
        return
    
    try:
        roll_no=int(input("Enter Roll Number to search: "))
        for student in students:
            if student["roll_no"]==roll_no:
                print("\nStudent found!")
                print("-"*60)
                
                print(f"Roll Number : {student['roll_no']}")
                print(f"Name : {student["name"]}")
                print(f"Age : {student['age']}")
                print(f"Grade : {student['grade']}")
                
                print("\nMarks:")
                for subject, marks in student['marks'].items():
                    print(f"{subject}:{marks}")
                
                print(f"\nTotal : {student['total']}")
                print(f"Percentage : {student['percentage']:.2f}%")
                return
        
        print("Student Not Found")
        
    except ValueError:
        print("Invalid input! Roll Number must be an integer.")
                
def update_marks():
    print("\n==================== Update Student Marks ==================")
    if len(students)==0:
        print("\nNo students found in record")
        return

    try:
        roll_no=int(input("Enter Roll Number:"))
        for student in students:
            if student['roll_no']==roll_no:
                print("\nStudent Found")
                print("\nCurrent Marks:")
                
                for subject,marks in student["marks"].items():
                    print(f"{subject} : {marks}")
                
                print("\nEnter New Marks:")
                
                math_marks=float(input("Enter Math Marks:"))
                physics_marks=float(input("Enter Physics Marks:"))
                chemistry_marks=float(input("Enter Chemistry Marks:"))
                
                student["marks"]["Math"]=math_marks
                student["marks"]["Physics"]=physics_marks
                student["marks"]["Chemistry"]=chemistry_marks
                
                total=math_marks+physics_marks+chemistry_marks
                
                percentage=total/3
                student["total"]=total
                student["percentage"]=percentage
                
                print("Marks Updated Successfully")
                
                return
            print("Student Not Found")
        
    except ValueError:
        print("Invalid Input! Please Enter Numeric Number")         

def delete_record():
    print("===================== DELETE RECORD ====================")   
    if len(students)==0:
        print("No record Found")
        return
    
    try:
        roll_no=int(input("Enter Roll Number to delete:"))
        for student in students:
            if student['roll_no']==roll_no:
                print("\nStudent Found")
                print(f"Name: {student['name']}")
                confirm=input("Are you sure you want to delete(Y/N):")
                if confirm.upper()=='Y':
                    students.remove(student)
                    print("student record deleted Successfully")
                
                else:
                    print("Deletion Canceled")
                
                return
        
        print("Student Not Found")
    
    except ValueError:
        print("Invalid Input! Roll Number must be Integer")

def main():
    while True:
        print("\n=========================================================")
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print("=========================================================")

        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search Student By Roll Number")
        print("4. Update Student Marks")
        print("5. Delete Student Records")
        print("6. Exit")

        
        
        print("==========================================================")
        
        choice= input("\nEnter your Choice (1-6):")
        
        if choice=="1":
            add_student()
        
        elif choice=="2":
            view_student()
        
        elif choice=="3":
            search_student()
        
        elif choice=="4":
            update_marks()
            
        elif choice=="5":
            delete_record()
        
        elif choice=="6":
            print("Thank You for using the system")
            break
        
        else:
            print("Invalid Choice! Please Enter between 1 to 6.")
        
        
        
        
        # def add():
            
        # def view():
        
        # def search():
        
        # def update():
        
        # def delete():
        
        
main()