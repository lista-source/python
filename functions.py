def salutation():
    print("Hello, Good Morning!")

salutation()

def greeting(name):
    print(f'Good Morning {name}!')

greeting('Lynn')
greeting('Juliana')
greeting('Anne')
def my_func(first_name, age):
    print(f'Hello,My name is, {first_name} and i am {age} years old!')
my_func('Juliana', 18)
my_func('Anne', 19)
my_func('Lynn', 21)
def sum_numbers(num1, num2):
    # print(num1 + num2)
    print(f'The sum is  {num1 + num2}')
sum_numbers(2, 61)
sum_numbers(3, 31)
sum_numbers(4, 2)
def multiply_numbers(num1, num2):
    # print(num1 * num2)
    result = num1 * num2
    return result
    # print(f'The multiplication is  {num1 * num2}')
print(multiply_numbers(2, 6))
print(multiply_numbers(3, 31))
print(multiply_numbers(4, 2))

def calculate_bmi(height_m, weight_kg):
    return weight_kg / (height_m ** 2)
def category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
the_bmi = calculate_bmi(1.2, 70)
print(f'BMI:{the_bmi}, category: {category(the_bmi)}')
