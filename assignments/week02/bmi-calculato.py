


def bmicalcuation():
    height = float(input("please enter your height(M):  "))
    weight = float(input("please enter your weight(KG):  "))
    bmi = float(weight/(height**2))
    if bmi < 18.5:
        print("Underweight")
    elif bmi > 18.5 and bmi < 25.0:
        print("Normal weight")
    elif bmi > 25.0 and bmi < 30.0:
        print("Overweight")
    else:
        print("Obese")

print("### welcome to bmi calcuation machine ###")
bmicalcuation()