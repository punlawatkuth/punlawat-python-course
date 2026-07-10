print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
height = (float(input("  -enter your height(meters)")))
weight = (float(input("  -enter your weight(killograms)")))

#process
BMI = weight / (height ** 2)

#output
print(f"your bmi is {BMI}")
