class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.__marks = marks #private and protected
        self.__age = age

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            return marks
        else:
            print("Invalid marks")

    def set_age(self, age):
        if age >= 18 and age <= 29:
            self.__age = age
            return age
        else:
            print("Invalid age")

student1 = Student("Andrew", 60,19)
print(student1.set_marks(70))
print(student1.set_age(30))
# print(student1.marks)
# student1.marks = 70
# print(student1.marks)
# student1.marks = -50
# print(student1.marks)