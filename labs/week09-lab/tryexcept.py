# added this for the lecture
# 3 types of error, logic error, runtime error, syntax error
# another type of errors, value error EX: 20 and "Twenty" (int) (string) does not go together, ZerodivisionError: cannot be divided by zero, FileNotFoundException, PermissionException
# try, except is a way of handling error in a way to prevent user error
# can be combined and akimbo together 
# testing first code: EX: SAFELY CALCULATE 2 INPUT 1 OPERAND IF ANYMORE THAN + - * / raise valueerror no divide by 0 end with finally
first_num = int(input("please input your numbers here (numerics only): "))
second_num = input(int("please input your numbers here (numerics only): "))
Operand = input("please select your operand (+ - * /)")
result = 0
if Operand == "+":
    result = first_num + second_num
elif Operand == "-":
    result = first_num - second_num
elif Operand == "*":
    result = first_num * second_num
elif Operand == "/":
    result = first_num * second_num
print(f"Your input {first_num} {Operand} {second_num} = {result}")

try:
    first_num = input(int("please input your numbers here (numerics only): "))
    second_num = input(int("please input your numbers here (numerics only): "))
    Operand = input("please select your operand (+ - * /)")
    result = 0
    if Operand == "+":
        result = first_num + second_num
    elif Operand == "-":
        result = first_num - second_num
    elif Operand == "*":
        result = first_num * second_num
    elif Operand == "/":
        result = first_num * second_num
    else:
        raise ValueError("Operand needs to be as noted")
    print(f"Your input {first_num} {Operand} {second_num} = {result}")
except ValueError:
    print("please only do numerics")
except ZeroDivisionError:
    print("please dont divide by 0")
except Exception:
    print("wallahi")
else:
    print("everything has been calculated")
finally:
    print("end of program")