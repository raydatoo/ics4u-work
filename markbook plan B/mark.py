home = {"12u":{"class_name" : "12u", "course_code" : "ics4u", "period" : 1, "teacher_name" : "gallo", "students": {"jack": {"first_name" : "jack", "last_name":"mathews"}}}}
a = 5
def add_class(class_name, course_code, period, teacher_name):
        class_info = {"class_name" : class_name, "course_code" : course_code, "period" : period, "teacher_name" : teacher_name, "students": {}}
        home[class_name] =class_info

def delete_class(class_name):
    if class_name in home:
        home.pop(class_name)

def edit_class(room, key, new_value):
    home[room][key] = new_value
    

def add_student(room, first_name, last_name, gender, student_number, grade, email, marks, comments):
    home[room]["students"][first_name] = {"first_name": first_name, "last_name":last_name , "gender": gender, "student_number": student_number, "grade": grade, "email": email, "marks": marks, "Comments": comments}

def terminate_student(room, student_name):
    home[room]["students"].pop(student_name)

def edit_student(room, student_name, key, new_value):
    home[room]["students"][student_name][key] = new_value

def view_home():
    for key in home.keys():
        print("_"*40)
        print((key),"|",(home[key]["course_code"]),"|",(home[key]["period"]),"|",(home[key]["teacher_name"]))
        


        




while a == 5:
    print("")
    print("")
    print("")
    action = input("what u want do")
    if action == "add class":
        add_class(input("enetr name"),input("eneter code"),input("endter period"),input("enter teacher"))
    elif action == "remove class":
        delete_class(input("eneter class name"))
    elif action == "edit class":
        edit_class(input("enter class"), input("enter key"), input("enter new value"))
    elif action == "add student":
        add_student(input("enter class"), input("first"), input("last"), input("gender"), input("num"), input("grade"), input("email"), input("marks"), input("comments"))
    elif action == "delete student":
        terminate_student(input("class"), input("first name"))
    elif action == "edit student":
        edit_student(input("class"), input("name"), input("key"), input("new value"))
    elif action == "home":
        view_home()
    

    


    



