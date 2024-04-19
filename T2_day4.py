class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):

        return f"{self.name}({self.age})"
    
p2 = person("John",21)
p3 = person("Sally",19)

print(p2)
print(p3)


p4 = person("John",39)
print(p4.name,"\n",p4.age)

#Activity 1
class Dog:
    def bark(self):
        print("woof")

my_dog = Dog()

my_dog.bark()



class Student():
    def __init__(student,name,score):

        student.name = name
        student.score = score

    def calculate_grade(student):
        ave_score = sum(student.score)/len(student.score)

        if ave_score > 89:
            return f"{student.name} has achieved {ave_score} with a code A+"
        elif ave_score > 79 and ave_score < 90:
           return f"{student.name} has achieved {ave_score} with a code B"
        elif ave_score > 69 and ave_score < 80:
           return f"{student.name} has achieved {ave_score} with a code C"
        elif ave_score > 59 and ave_score < 70:
           return f"{student.name} has achieved {ave_score} with a code D"
        elif ave_score < 60:
           return f"{student.name} has achieved {ave_score} with a code F"
        
marks = [85,90,88,92,95]
Student1 = Student("Alice",marks)

print(Student1.calculate_grade())


    

        


        