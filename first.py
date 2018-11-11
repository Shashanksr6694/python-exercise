def age_fun(age):
    new_age = age + 50
    return new_age

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error divide by zero"


age=float(input("Enter your age"))

if age < 150:
    print(age_fun(age))
else:
    print("That's impossible")
