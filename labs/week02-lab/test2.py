print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")


#input
seconds = int(input("   - Enter the number of seconds: "))


#process
hours = seconds // 3600
second_remain = seconds % 3600

minute = second_remain // 60
second_remain = minute * 60


#output
print(f" {seconds} seconds = {hours} hour, {minute} minute, {second_remain} second")