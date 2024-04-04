def create_student_dict():
    student_dict = {
        "Luvuyo" : 19,
        "Ross" : 20,
        "Zaid" : 19,
        "Adam" : 18
    }
    return student_dict

def access_age(student_dict, student_name):
    if student_name in student_dict:
        return student_dict[student_name]
    else:
        return None
    
def add_student(student_dict, student_name, student_age):
    student_dict[student_name] = student_age
    print(f"{student_name} added to dictionary.")

def update_age(student_dict,student_name,new_age):
    if student_name in student_dict:
        student_dict[student_name] = new_age
        print(f"Age of {student_name} updated to {new_age}.")
    else:
        print(f"{student_name} not found in dictionary")

def remove_student(student_dict,student_name):
    if student_name in student_dict:
        del student_dict[student_name]
        print(f"{student_name} removed from the dictionary")

def main():
    students = create_student_dict()
    print("Age of Ross", access_age(students, "Ross"))
    add_student(students, "Alex", 18)
    update_age(students, "Luvuyo",20)
    remove_student(students,"Zaid")
    print(students)

if __name__ == "__main__":
    main()