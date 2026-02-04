votes = 0
if votes > 10000:
    print("You are elected as a Governor")
else:
    print("You are  not elected as a Governor")

temperature = float(input("What is your temperature in degrees celsius?"))
if temperature > 30:
    print("it ia a hot day")
else:
    print("it ia a fairly warm day")

age = int(input("What is your age?"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

score = 0
if score >= 80 and score <= 100:
    print("You have grade A")
elif score >= 65 and score <= 80:
    print("You have grade B")
elif score >= 50 and score <= 65:
    print("You have grade C")
elif score >= 30 and score <= 50:
    print("You have grade D")
elif score <=0 and score < 30:
    print("You have grade E")
else:
    print("Please enter a number between 0 and 100")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
bmi = weight / (height ** 2)
print(bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 18.5 and bmi < 25:
    print("You are normal weight")
elif bmi <= 25 and bmi < 30:
    print("You are over weight")
else:
    print("You are obese")