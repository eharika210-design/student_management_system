students=[]
while True:
    print("\n=====STUDENT MANAGEMENT SYSTEM=====")
    print("1.add student")
    print("2.view students")
    print("3.exit")
    choice=input("enter your choice:")
    if choice=="1":
        roll =input("enter roll number:")
        name = input("enter name:")
        marks = input("enter marks:")
        student ={
            "roll":roll,
            "name":name,
            "marks":marks,
        }
        students.append(student)
        print("student added successfully!")
    elif choice=="2":
        print("\nstudent records:")
        for student in students:
            print(student)
    elif choice=="3":
        print("thank you!")
        break
    else:
        print("invalid choice!")
