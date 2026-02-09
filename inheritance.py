class Employee:
    def __init__(self, name,gender,age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, gender, age, salary, prog_language):
        super().__init__(name, gender, age, salary)
        self.prog_language = prog_language
    def calculate_bonus(self):
        if self.prog_language == "Python":
            bonus_rate = 0.15
            return bonus_rate*self.salary
        elif self.prog_language == "Kotlin":
            bonus_rate = 0.12
            return bonus_rate*self.salary
        else:
            bonus_rate = 0.10
            return bonus_rate*self.salary

developer1 = Developer("David", "Male", 20, 120000,"Python")
print(developer1.calculate_bonus())

developer2 = Developer("Angela", "Female", 23, 140000,"Kotlin")
print(developer2.calculate_bonus())

developer3 = Developer("Dan", "Male", 18, 130000,"C++")
print(developer3.calculate_bonus())
