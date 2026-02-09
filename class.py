class Person:
    def __init__(self, name, gender, marital_status, occupation, salary, birth_year):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation
        self.salary = salary
        self.birth_year = birth_year
    def annual_salary(self):
        return self.salary * 12
    def calculate_tax(self, tax_rate):
        return self.salary * tax_rate
        # return self.annual_salary() / 12
    def calculated_age(self, current_year):
        return current_year - self.birth_year
person1 = Person("John", "Male", "Single", "Doctor",500000,2008)
print(person1.annual_salary())
print(person1.calculate_tax(0.01))
print(person1.calculated_age(2026))
person2 = Person("Esther", "Female", "Married", "Nurse",240000, 2001)
print(person2.annual_salary())
print(person2.calculate_tax(0.01))
print(person2.calculated_age(2026))
person3 = Person("Andy", "Male", "Divorced", "Developer", 320000, 2004)
print(person3.annual_salary())
print(person3.calculate_tax(0.01))
print(person3.calculated_age(2026))
# print(person1.name)
print(person1.gender)
# print(person1.marital_status)
# print(person1.occupation)
# print(person2.name)
# print(person2.gender)
# print(person2.marital_status)
# print(person2.occupation)
# print(person3.name)
# print(person3.gender)
print(person3.marital_status)
# print(person3.occupation)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
car1 = Car("Ford", "Mustang", 1999)
car2 = Car("Toyota", "Toyota Camry", 2009)
car3 = Car("BMW", "BMW 3 Series", 2020)
car4 = Car("Bentley", "Azure", 2012)
# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car2.make)
# print(car2.model)
# print(car2.year)
# print(car3.make)
# print(car3.model)
# print(car3.year)
# print(car4.make)
# print(car4.model)
# print(car4.year)
